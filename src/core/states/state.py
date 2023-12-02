import pygame
from core.connection import Network


class State:
    """Clase base para los estados del juego."""

    def __init__(self, client):
        """Inicializa un nuevo estado del juego.

        Args:
            client: Cliente del juego.
        """
        from core.client import Client

        self._client: Client = client

    def init(self):
        """Inicializa el estado. Puede ser llamado varias veces para reiniciar el estado."""
        pass

    def update(self, dt: float):
        """Actualiza el estado.

        Args:
            dt (float): Delta de tiempo. Tiempo desde el último fotograma.
        """
        pass

    def update_server(self, network: Network):
        """Actualiza el servidor."""
        pass

    def draw(self, surface: pygame.Surface):
        """Dibuja el estado.

        Args:
            surface (pygame.Surface): Superficie en la que se dibujará el estado.
        """
        pass
