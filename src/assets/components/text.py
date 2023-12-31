import pygame
from .component import Component

class Text(Component):
    def __init__(self,
                 text: str,
                 x: int, y: int,
                 font: str = "ThaleahFat",
                 font_size: int = 12,
                 font_color: tuple[int, int, int] | str = "white",
                 align: str = "topleft"):
        """
        Inicializa un componente de texto en el juego.

        Args:
            text (str): El texto que se mostrará.
            x (int): Posición x del texto.
            y (int): Posición y del texto.
            font (str, opcional): Fuente del texto. Por defecto es "ThaleahFat".
            font_size (int, opcional): Tamaño de la fuente. Por defecto es 12.
            font_color (tuple[int, int, int] | str, opcional): Color de la fuente. Por defecto es "white".
            align (str, opcional): Alineación del texto. Por defecto es "topleft".
        """
        # Texto
        self._text = text
        self._font = pygame.font.Font(f"./src/assets/fonts/{font}.ttf", font_size)
        self._font_color = font_color

        # Posición
        self._x = x
        self._y = y
        self._align = align

    def _render_text(self) -> tuple[pygame.Surface, pygame.Rect]:
        """
        Renderiza el texto en una superficie y rectángulo.

        Returns:
            tuple[pygame.Surface, pygame.Rect]: Superficie y rectángulo del texto renderizado.
        """
        surface = self._font.render(self._text, True, self._font_color)
        rect = surface.get_rect()

        if self._align == "topleft":
            rect.topleft = (self._x, self._y)
        elif self._align == "center":
            rect.center = (self._x, self._y)

        return surface, rect

    def update(self, dt: float):
        """
        Actualiza el componente de texto.

        Args:
            dt (float): Delta time. Tiempo desde el último frame.
        """
        pass

    def draw(self, surface: pygame.Surface):
        """
        Dibuja el componente de texto en la superficie especificada.

        Args:
            surface (pygame.Surface): Superficie donde se dibujará el texto.
        """
        text, rect = self._render_text()
        surface.blit(text, rect)
