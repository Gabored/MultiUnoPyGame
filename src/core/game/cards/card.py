import pygame

from core.graphics import Resources


class CardColor:
    RED = "rojo"
    BLUE = "azul"
    GREEN = "verde"
    YELLOW = "amarillo"
    WILD = "comodin"


class Card:
    """Clase base para las cartas del juego."""

    _images_cache: dict[str, pygame.Surface] = {}

    def __init__(self, color: str, value: str):
        """Inicializa una carta del juego.

        Args:
            color (str): Color de la carta.
            value (str): Valor de la carta.
        """
        self._color = color
        self._value = value

        self._name = f"{self._color}-{self._value}"
        self._image_path = f"src/assets/images/cards/{self._color}/{self._value}.png"

    @property
    def color(self) -> str:
        """Obtiene el color de la carta.

        Returns:
            str: Color de la carta.
        """
        return self._color

    @property
    def name(self) -> str:
        """Obtiene el nombre de la carta.

        Returns:
            str: Nombre de la carta.
        """
        return self._name

    @property
    def image(self) -> pygame.Surface:
        """Obtiene la imagen de la carta.

        Returns:
            pygame.Surface: Imagen de la carta.
        """
        if self._name not in self._images_cache:
            self._images_cache[self._name] = self.load_image()
        return self._images_cache[self._name]

    def load_image(self):
        """Carga la imagen de la carta desde los recursos.

        Returns:
            pygame.Surface: Imagen escalada de la carta.
        """
        img = Resources.CARDS[self._color][self._value + ".png"]
        return pygame.transform.scale(img, (int(img.get_width() * 3.5), int(img.get_height() * 3.5)))

    def play(self, game):
        """Define la acción de jugar la carta en el juego.

        Args:
            game: Referencia al juego en el que se está jugando la carta.
        """
        pass
