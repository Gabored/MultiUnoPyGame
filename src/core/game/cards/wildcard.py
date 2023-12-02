from .card import Card, CardColor


class WildCard(Card):
    def __init__(self):
        """Inicializa una carta "Wild" (comodín) del juego.

        La carta "Wild" permite al jugador elegir el color que desee.

        """
        super().__init__("wild", "select_color")

    def play(self, game):
        """Define la acción de jugar la carta "Wild" en el juego.

        Args:
            game: Referencia al juego en el que se está jugando la carta.
        """
        pass
