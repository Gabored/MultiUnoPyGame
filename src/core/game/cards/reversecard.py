from .card import Card, CardColor


class ReverseCard(Card):
    def __init__(self, color: str):
        """Inicializa una carta "Reverse" (cambio de dirección) del juego.

        Args:
            color (str): Color de la carta.

        Raises:
            ValueError: Si se proporciona un color inválido.
        """
        if color not in [CardColor.RED, CardColor.BLUE, CardColor.GREEN, CardColor.YELLOW]:
            raise ValueError(f"Color inválido: {color}")

        super().__init__(color, "reverse")

    def play(self, game):
        """Define la acción de jugar la carta "Reverse" en el juego.

        Args:
            game: Referencia al juego en el que se está jugando la carta.
        """
        pass
