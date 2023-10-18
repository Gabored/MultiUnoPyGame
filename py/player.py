from card import Card
from termcolor import colored

class Player:
    '''Player Class that will represent a Playable Instance of a Game of UNO'''
    def __init__(self, name:str, hand:Card=None) -> None:
        self.name = name
        self.hand = hand

    def print_hand(self):
        ''' Player Method that implements colored print using termcolor that prints card.action and card.number in respective colors'''
        for card in self.hand:
            if card.number == None:
                print(colored(card.action, card.color))
            else: 
                print(colored(card.number, card.color))
    
    def check_card_in_hand(self, card: str, topOfStack: Card):
        ''' Function that checks if attribute Card matches an instance on Players Hand'''
        for c in self.hand:
            if topOfStack != None:
                if c.__repr__() == card and (topOfStack.color == c.color or topOfStack.number == c.number) : #Check if color or number matches
                    print ("Here!!")
                    return True
            else: 
                if c.__repr__()  == card: 
                    ("topofstack none")
                    return True
        return False
    
    def find_card_in_hand(self, card_input, topOfStack):
        for card in self.hand:
            if topOfStack is None:
                if card.__repr__() == card_input:
                    return card
            elif card.__repr__() == card_input and (topOfStack.color == card.color or topOfStack.number == card.number):
                return card
        return None
    

    def pop_card(self, card: str):
        ''' Removes a specific instance of card.__repr__() from deck'''
        return self.hand.remove(card)

    
        
        



             
