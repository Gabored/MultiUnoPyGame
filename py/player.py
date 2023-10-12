from card import Card
from termcolor import colored

class Player:
    '''Player Class that will represent a Playable Instance of a Game of UNO'''
    def __init__(self, name:str, hand:Card) -> None:
        self.name = name
        self.hand = hand

    def print_hand(self):
        ''' Player Method that implements colored print using termcolor that prints card.action and card.number in respective colors'''
        for card in self.hand:
            if card.number == None:
                print(colored(card.action, card.color))
            else: 
                print(colored(card.number, card.color))

    def card_input(self, topOfStack: Card):
        ''' Player Method that ask the Player to input a card from it's hand and check if it's valid to play or if it exist'''
        card = input("Type the card you want to play: [format:number/name - color] :")
        while not self.check_card_in_hand(card, topOfStack):
            print("Card not found! check your hand or check format!")
            card = input("Type the card you want to play: [format:number/name - color] :")
        self.remove_card(card)
        return card
    
    def check_card_in_hand(self, card: str, topOfStack: Card):
        ''' Function that checks if attribute Card matches an instance on Players Hand'''
        for c in self.hand:
            if topOfStack != None:
                if c.__repr__() == card and (topOfStack.color == c.color or topOfStack.number == c.number) :
                    return True
            else: 
                if c.__repr__() == card:
                    return True
        return False
    

    def remove_card(self, card: str):
        ''' Removes a specific instance of card.__repr__() from deck'''
        for c in self.hand:
            if c.__repr__() == card:
                self.hand.remove(c)
                break
    
        
        



             
