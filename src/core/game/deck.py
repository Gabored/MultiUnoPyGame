import random
from .cards import (
    Card, CardColor, NumberCard,
    DrawTwoCard, SkipCard, ReverseCard,
    WildCard, WildDrawFourCard
)


class Deck:
    """Clase que representa la baraja del juego. Esencialmente, una cola de cartas,
    ya que las cartas se toman de la parte superior y se colocan en la parte inferior del mazo."""

    __cards: list[Card]

    def __init__(self):
        self.__cards = []
        for color in [CardColor.RED, CardColor.GREEN, CardColor.BLUE, CardColor.YELLOW]:
            for number in range(10):
                for _ in range(2):
                    self.__cards.append(NumberCard(color=color, value=str(number)))

            for _ in range(2):
                self.__cards.append(DrawTwoCard(color=color))
                self.__cards.append(SkipCard(color=color))
                self.__cards.append(ReverseCard(color=color))

        for _ in range(4):
            self.__cards.append(WildCard())
            self.__cards.append(WildDrawFourCard())

        self.shuffle()

    def shuffle(self):
        """Baraja las cartas del mazo"""

        random.shuffle(self.__cards)

    def draw_card(self) -> Card:
        """Saca una carta de la parte superior del mazo"""

        return self.__cards.pop()

    def push(self, card: Card) -> None:
        """Coloca una carta en la parte inferior del mazo"""

        self.__cards.insert(0, card)
