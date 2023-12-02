from .card import Card, CardColor


class NumberCard(Card):
    def __init__(self, color: str, value: str):
        """Inicializa una carta numérica del juego.

        Args:
            color (str): Color de la carta.
            value (str): Valor de la carta.

        Raises:
            ValueError: Si se proporciona un color o un valor inválido.
        """
        if color not in [CardColor.RED, CardColor.BLUE, CardColor.GREEN, CardColor.YELLOW]:
            raise ValueError(f"Color inválido: {color}")

        if value not in [str(i) for i in range(10)]:
            raise ValueError(f"Valor inválido: {value}")

        super().__init__(color, value)

    def play(self, game):
        """Define la acción de jugar la carta numérica en el juego.

        Args:
            game: Referencia al juego en el que se está jugando la carta.
        """
        pass
