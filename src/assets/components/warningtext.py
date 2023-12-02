import pygame
from util import lerp
from .text import Text

class WarningText(Text):
    def __init__(self,
                 text: str,
                 x: int, y: int,
                 lifespan: int = 1000,
                 font: str = "ThaleahFat",
                 font_size: int = 12,
                 font_color: tuple[int, int, int] | str = "white",
                 align: str = "topleft"):

        """
        Inicializa un componente de texto de advertencia en el juego.

        Args:
            text (str): El texto de la advertencia.
            x (int): Posición x del texto.
            y (int): Posición y del texto.
            lifespan (int, opcional): Duración de la advertencia en milisegundos. Por defecto es 1000.
            font (str, opcional): Fuente del texto. Por defecto es "ThaleahFat".
            font_size (int, opcional): Tamaño de la fuente. Por defecto es 12.
            font_color (tuple[int, int, int] | str, opcional): Color de la fuente. Por defecto es "white".
            align (str, opcional): Alineación del texto. Por defecto es "topleft".
        """

        super().__init__(text, x, y, font, font_size, font_color, align)

        # Tiempo de exhibición
        self.__lifespan = lifespan

        # Tiempo desde el inicio
        self.__created_at = pygame.time.get_ticks()

        # Animación
        self.__init_y = y
        self.__alpha = 255

    @property
    def is_expired(self) -> bool:
        """
        Verifica si el tiempo de vida de la advertencia ha expirado.

        Returns:
            bool: True si la advertencia ha expirado, False en caso contrario.
        """
        return pygame.time.get_ticks() - self.__created_at > self.__lifespan

    def update(self, dt: float):
        """
        Actualiza la posición y la transparencia de la advertencia.

        Args:
            dt (float): Delta time. Tiempo desde el último frame.
        """
        self._y = lerp(self._y, self.__init_y - 35, 0.02)
        self.__alpha = lerp(self.__alpha, 0, 0.02)

    def draw(self, surface: pygame.Surface):
        """
        Dibuja la advertencia en la superficie especificada.

        Args:
            surface (pygame.Surface): Superficie donde se dibujará la advertencia.
        """
        text, rect = self._render_text()
        text.set_alpha(self.__alpha)  # Define la transparencia
        surface.blit(text, rect)
