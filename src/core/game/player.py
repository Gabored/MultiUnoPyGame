from .cards.card import Card

class Player:
    __id: int
    __name: str
    __hand: list[Card]

    def __init__(self, id: int, name: str):
        """Clase que representa a un jugador del juego."""
        
        self.__id = id
        self.__name = name
        self.__hand = []

    @property
    def id(self) -> int:
        """Obtiene el ID del jugador."""

        return self.__id

    @property
    def name(self) -> str:
        """Obtiene el nombre del jugador."""

        return self.__name

    @property
    def hand(self) -> list[Card]:
        """Obtiene la mano del jugador, que contiene las cartas que tiene en su poder."""

        return self.__hand

    def add_card(self, card: Card) -> None:
        """Añade una carta a la mano del jugador.

        Args:
            card (Card): Carta que se añadirá a la mano del jugador.
        """

        self.__hand.append(card)
