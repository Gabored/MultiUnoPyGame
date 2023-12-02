import pygame

from assets.components import WarningText, Button
from core.game.player import Player
from core.game.match import Match
from core.graphics import Resources
from core.connection import Network

from .menu import Menu
from .state import State


class Party(State):
    __id: int
    __match: Match | None

    # Salvando objetos do pygame para não precisar carregar toda hora
    __flipped_cards: dict[str, pygame.Surface]
    __font: pygame.font.Font

    def __init__(self, client):
        """Inicializa el estado de la partida."""
        super().__init__(client)
        self.__match = None
        self.__id = -1

        # Redimensionar y rotar las cartas
        card_width = int(Resources.CARD_BACK.get_width() * 3.5)
        card_height = int(Resources.CARD_BACK.get_height() * 3.5)
        size = (card_width, card_height)

        self.__flipped_cards = {
            "izquierda": pygame.transform.rotate(pygame.transform.scale(Resources.CARD_BACK, size), -90).convert(),
            "derecha": pygame.transform.rotate(pygame.transform.scale(Resources.CARD_BACK, size), 90).convert(),
            "arriba": pygame.transform.rotate(pygame.transform.scale(Resources.CARD_BACK, size), 180).convert(),
            "abajo": pygame.transform.scale(Resources.CARD_BACK, size).convert(),
        }

        self.__font = pygame.font.Font(f"./src/assets/fonts/ThaleahFat.ttf", 28)

    def init(self):
        """Inicializa los componentes de la partida."""
        self._client.add_component(
            Button("x", self._client.width - 20, 20, font_size=30, align="center",
                   width=30, height=30, animation=None, on_click=self.__exit_party))

        if self._client.network.id == 0:
            self._client.add_component(
                Button("> Comenzar", self._client.width // 2, self._client.height // 2, font_size=48, align="center",
                       font_color="#FFD800", hover_color="#FFEE75", width=200, height=50,
                       animation="up", on_click=self.__start_party), id="start")

    def __start_party(self, *_):
        """Comienza la partida si hay suficientes jugadores."""
        if self.__match.get_number_of_players() < 2:
            self._client.add_component(
                WarningText("Necesitas al menos 2 jugadores", self._client.width // 2, 370,
                            font_size=30, align="center"), id="left")
            return

        self._client.network.send({"type": "START"})
        self._client.pop_component("start")

    def __exit_party(self, *_):
        """Abandona la partida y regresa al menú principal."""
        self._client.disconnect()
        self._client.close_server()
        self._client.state = Menu(self._client)

        if not self._client.get_component("left"):
            self._client.add_component(
                WarningText("Abandonaste la partida", self._client.width // 2, 550,
                            font_size=30, align="center"), id="left")

    def update(self, dt: float):
        """Actualiza el estado de la partida."""
        if self.__match is None:
            return

        if not self.__match.host_online:
            self.__exit_party()
            self._client.add_component(
                WarningText("El anfitrión abandonó la partida", self._client.width // 2, 550,
                            font_size=30, align="center"), id="left")
    def update_server(self, network: Network):
        """Actualiza el servidor y la partida."""
        if network is None:
            return

        # Si la partida ya ha comenzado, regresar al menú de join
        self.__id = network.id
        if self.__id == -1:
            self.__exit_party()
            return

        match = network.send({"type": "GET"})
        if match is not None:
            self.__match = match

    def __draw_hand(self, surface: pygame.Surface, player: Player, position: str):
        """Dibuja la mano de cartas del jugador en la pantalla."""
        def get_vpos(hd: int, j: int) -> int:
            return y - hd // 2 + j * space

        def get_hpos(hd: int, j: int) -> int:
            return x - hd // 2 + j * space

        flipped_card = self.__flipped_cards[position]
        card_dimension = flipped_card.get_width() if position in ("top", "bottom") else flipped_card.get_height()

        # Define la posición de las cartas en la pantalla
        match position:
            case "left":
                x = 20
                y = self._client.height // 2
            case "right":
                x = self._client.width - 20 - flipped_card.get_width()
                y = self._client.height // 2
            case "top":
                x = self._client.width // 2
                y = 20
            case "bottom":  # Propia mano
                x = self._client.width // 2
                y = self._client.height - 20 - flipped_card.get_height()
            case _:
                return

        max_space = -30
        max_dimension = 600 if position in ("top", "bottom") else 400

        space = min(card_dimension + max_space, max_dimension // len(player.hand))
        hand_dimension = (len(player.hand) - 1) * space + card_dimension
        for i, card in enumerate(player.hand):
            match position:
                case "top":
                    surface.blit(flipped_card, (get_hpos(hand_dimension, i), y))
                case "bottom":
                    card_image = card.image if self.__match.ready else flipped_card
                    surface.blit(card_image, (get_hpos(hand_dimension, i), y))
                case "left" | "right":
                    surface.blit(flipped_card, (x, get_vpos(hand_dimension, i)))

        if player.name.lower() in ("Gabo", "Axel"):
            name = f"{player.name} (Host)" if player.id == 0 else \
                f"{player.name} (You)" if position == "bottom" else player.name
            color = "cyan"
        else:
            name = f"{player.name} (You)" if position == "bottom" else player.name
            color = "yellow" if player.id == 0 else "white"

        text = self.__font.render(name, True, color)
        rect = text.get_rect()

        match position:
            case "top":
                rect.midtop = (x, y + flipped_card.get_height() + 5)
            case "bottom":
                rect.midbottom = (x, y - 5)
            case "left" | "right":
                rect.midbottom = (x + flipped_card.get_width() // 2, y - hand_dimension // 2 - 5)

        surface.blit(text, rect)

    def __draw_cards(self, surface: pygame.Surface):
        """
        Dibuja las manos de los jugadores en la superficie del juego.

        Args:
            surface (pygame.Surface): Superficie de Pygame en la que se dibujarán las manos de los jugadores.
        """
        # Obtiene la cantidad de jugadores
        players_len = self.__match.get_number_of_players()

        # Configuración de posiciones según la cantidad de jugadores
        offsets = {
            2: ["arriba"],
            3: ["izquierda", "derecha"],
            4: ["izquierda", "derecha", "arriba"]
        }

        positions = offsets.get(players_len, [])

        for position in positions:
            # Calcula el identificador del jugador según la posición
            player_id = (self.__id + 1) % players_len if position == "izquierda" or players_len == 2 else \
                (self.__id - 1) % players_len if position == "derecha" else \
                (self.__id + 2) % players_len if position == "arriba" else None

            if player_id is not None:
                player = self.__match.get_player(player_id)
                if player is not None and player.hand:
                    self.__draw_hand(surface, player, position)

        player = self.__match.get_player(self.__id)
        if player.hand:
            # TODO: Hacer las cartas interactivas
            self.__draw_hand(surface, player, "abajo")

    def draw(self, surface: pygame.Surface):
        """
        Dibuja las cartas en la superficie del juego.

        Args:
            surface (pygame.Surface): Superficie de Pygame en la que se dibujarán las cartas.
        """
        # Dibuja el fondo en la superficie
        surface.blit(Resources.BACKGROUND, (0, 0))

        if self.__match is None:
            return

        # Dibuja las cartas en la superficie
        self.__draw_cards(surface)
