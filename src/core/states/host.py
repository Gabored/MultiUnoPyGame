import pygame

from core.graphics import Resources
from core.connection import Network
from assets.components import Text, Button, TextInput, WarningText

from .party import Party
from .state import State


class Host(State):
    """Representa el estado para hospedar una partida en LAN."""

    __cards: list[pygame.Surface]

    def __init__(self, client):
        """Inicializa el estado de hospedar partida.

        Args:
            client: Cliente del juego.
        """
        super().__init__(client)
        self.__cards = [
            pygame.transform.rotate(Resources.CARD_WORLD_RESIZED, 15),
            pygame.transform.rotate(Resources.CARD_BACK_RESIZED, -15)
        ]

    def init(self):
        """Inicializa los componentes de la interfaz de usuario para hospedar partida."""
        cx = self._client.width // 2
        cy = self._client.height // 2

        self._client.add_component(
            Text("Hospedar una partida LAN", cx, 60, font_size=72, align="center"))

        self._client.add_component(
            Text("Nickname:", cx, 215, font_size=35, align="center"))
        self._client.add_component(
            TextInput(cx, 260, 300, 50, font_size=30,
                      max_length_input=10,
                      text_align="center", font_color="white", background_color="#a30f17",
                      border_color="#8c0d13", border_width=3, border_radius=5, align="center"),
            id="nickname")

        self._client.add_component(
            Text("Puerto:", cx, 310, font_size=35, align="center"))
        self._client.add_component(
            TextInput(cx, 355, 300, 50, font_size=30,
                      max_length_input=5, default="25565", numeric=True,
                      text_align="center", font_color="white", background_color="#a30f17",
                      border_color="#8c0d13", border_width=3, border_radius=5, align="center"),
            id="port")

        self._client.add_component(
            Button("> Iniciar Partida <", cx, 445, width=300, height=50,
                   font_size=40, align="center", animation="up",
                   on_click=self.__host_server))

        self._client.add_component(
            Button("< Volver", 10, 560, height=30, font_size=32, on_click=self._client.pop_state))

    def __host_server(self, _):
        nickname = self._client.get_component("nickname").text.strip()
        port = self._client.get_component("port").text

        if not self.__validate_nickname(nickname):
            self._client.add_component(
                WarningText("Nickname inválido", self._client.width // 2, 550,
                            font_size=30, align="center"))
            return

        if Network.port_in_use(port):
            self._client.add_component(
                WarningText("El puerto ya está en uso", self._client.width // 2, 550,
                            font_size=30, align="center"))
            return

        self._client.host_server(port)
        pygame.time.wait(500)  # Espera a que el servidor inicie
        self._client.connect("localhost", port)
        self._client.send({"type": "JOIN", "nickname": nickname})  # Envia el nickname al servidor

        self._client.state = Party(self._client)

    @staticmethod
    def __validate_nickname(nickname: str) -> bool:
        """Valida el nickname.

        Args:
            nickname (str): Nickname a validar.

        Returns:
            bool: True si el nickname es válido, False en caso contrario.
        """
        return 3 <= len(nickname) <= 10

    def update_server(self, network: Network):
        pass

    def draw(self, surface: pygame.Surface):
        """Dibuja los elementos en la superficie de la pantalla."""
        surface.blit(Resources.BACKGROUND, (0, 0))
        surface.blit(self.__cards[0], (40, 200))
        surface.blit(self.__cards[1], (610, 250))
