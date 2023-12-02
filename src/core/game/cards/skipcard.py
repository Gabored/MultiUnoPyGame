from .card import Card, CardColor


class SkipCard(Card):
    def __init__(self, color: str):
        """Inicializa una carta "Skip" (salto) del juego.

        Args:
            color (str): Color de la carta.

        Raises:
            ValueError: Si se proporciona un color inválido.
        """
        if color not in [CardColor.RED, CardColor.BLUE, CardColor.GREEN, CardColor.YELLOW]:
            raise ValueError(f"Color inválido: {color}")

        super().__init__(color, "skip")

    def play(self, game):
        """Define la acción de jugar la carta "Skip" en el juego.

        Args:
            game: Referencia al juego en el que se está jugando la carta.
        """
        pass
