import pygame


class Component:
    """Clase abstracta para los componentes del juego."""

    def update(self, dt: float):
        """Actualiza el componente.

        Args:
            dt (float): Delta time. Tiempo desde el último frame.
        """
        pass

    def on_keydown(self, event: pygame.event):
        """Evento de tecla presionada.

        Args:
            event (pygame.event): Evento de tecla presionada.
        """

    def draw(self, surface: pygame.Surface):
        """Dibuja el componente.

        Args:
            surface (pygame.Surface): Superficie donde se dibujará el componente.
        """
        pass
