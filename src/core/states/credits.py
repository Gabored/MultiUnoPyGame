import pygame

from core.graphics import Resources
from core.connection import Network
from assets.components import Text, Button

from .state import State


class Credits(State):
    """Representa el estado de los créditos del juego."""

    __cards: list[pygame.Surface]

    def __init__(self, client):
        """Inicializa el estado de los créditos.

        Args:
            client: Cliente del juego.
        """
        super().__init__(client)
        self.__cards = [
            pygame.transform.rotate(Resources.random_card(), 15),
            pygame.transform.rotate(Resources.random_card(), -15)
        ]

    def init(self):
        """Inicializa los componentes de la interfaz de usuario para la pantalla de créditos."""
        cx = self._client.width // 2
        cy = self._client.height // 2

        self._client.add_component(
            Text("Creditos", cx, 60, font_size=72, align="center"))

        self._client.add_component(
            Text("Profesor", cx, 170, font_size=50, align="center"))
        self._client.add_component(
            Text("Victor Hugo Martinez Sanchez", cx, 210, font_size=30, align="center"))

        self._client.add_component(
            Text("Estudiantes", cx, 290, font_size=50, align="center"))
        self._client.add_component(
            Text("Gabriel Olvera + Axel Orozco + Diego Moran", cx, 330, font_size=20, align="center"))

        self._client.add_component(
            Text("Universidad", cx, 410, font_size=50, align="center"))
        self._client.add_component(
            Text("ITESO", cx, 450, font_size=35, align="center"))

        self._client.add_component(
            Button("< Volver", 10, 560, height=30, font_size=32, on_click=self._client.pop_state))

    def update(self, dt: float):
        """Actualiza la lógica del estado."""
        pass

    def update_server(self, network: Network):
        """Actualiza el servidor."""
        pass

    def draw(self, surface: pygame.Surface):
        """Dibuja los elementos en la superficie de la pantalla."""
        surface.blit(Resources.BACKGROUND, (0, 0))
        surface.blit(self.__cards[0], (40, 130))
        surface.blit(self.__cards[1], (610, 210))
