from .player import Player
from .deck import Deck
from .cards import Card


class Match:
    __ready: bool
    __deck: Deck | None
    __players: list[Player]

    def __init__(self):
        """Clase que representa una partida del juego."""

        self.__ready = False
        self.__players = []
        self.__deck = Deck()

    @property
    def ready(self) -> bool:
        """Indica si la partida está lista para iniciar."""

        return self.__ready

    @property
    def host_online(self) -> bool:
        """Verifica si el anfitrión está en línea."""

        return 0 in [player.id for player in self.players]

    @property
    def players(self) -> list[Player]:
        """Obtiene la lista de jugadores en la partida."""

        return self.__players

    @property
    def deck(self) -> Deck:
        """Obtiene el mazo de cartas de la partida."""

        return self.__deck

    def is_full(self) -> bool:
        """Verifica si la partida está llena (tiene 4 jugadores)."""

        return len(self.__players) == 4

    def get_player(self, player_id: id) -> Player | None:
        """Obtiene un jugador por su ID.

        Args:
            player_id (int): ID del jugador.

        Returns:
            Player | None: Jugador correspondiente al ID o None si no se encuentra.
        """

        for player in self.__players:
            if player.id == player_id:
                return player
        return None

    def get_number_of_players(self) -> int:
        """Obtiene el número de jugadores en la partida."""

        return len(self.__players)

    def start(self) -> None:
        """Inicia la partida."""

        self.__ready = True

    def add_player(self, player_id: id, player_name: str) -> None:
        """Agrega un jugador a la partida.

        Args:
            player_id (int): ID del jugador.
            player_name (str): Nombre del jugador.
        """
        player = Player(id=player_id, name=player_name)

        # Distribuye 7 cartas a cada jugador al inicio del juego
        for _ in range(7):
            player.add_card(self.__deck.draw_card())
        self.__players.append(player)

    def remove_player(self, player_id: id) -> str | None:
        """Elimina a un jugador de la partida.

        Args:
            player_id (int): ID del jugador.

        Returns:
            str | None: Nombre del jugador eliminado o None si no se encuentra.
        """

        for player in self.__players:
            if player.id == player_id:
                # Devuelve las cartas del jugador al mazo
                for card in player.hand:
                    self.__deck.push(card)
                self.__players.remove(player)
                return player.name
        return None
