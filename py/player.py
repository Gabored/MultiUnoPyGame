from card import Card

class Player:
    '''Player Class that will represent a Playable Instance of a Game of UNO'''
    def __init__(self, name:str, hand:Card) -> None:
        self.name = name
        self.hand = hand
