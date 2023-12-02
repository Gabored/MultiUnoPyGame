from .card import Card, CardColor


class WildDrawFourCard(Card):
    def __init__(self):
        """Inicializa una carta "Wild Draw Four" (comodín que hace robar cuatro cartas) del juego.

        """
        super().__init__("wild", "draw4")

    def play(self, game):
        """Define la acción de jugar la carta "Wild Draw Four" en el juego.

        Args:
            game: Referencia al juego en el que se está jugando la carta.
        """
        pass
