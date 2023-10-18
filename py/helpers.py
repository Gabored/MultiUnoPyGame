from card import Card
import os
from termcolor import colored


def print_deck(deck: Card) -> None:
    '''Function that uses repr method of Card to print the deck in a legible form '''
    for card in deck:
        print(card.__repr__())

def clear():
    ''' Function of Clearing the Terminal'''
    # Clearing the Screen
    os.system('cls')

def colored_print(card: Card):
    ''' Print a Card Instance Using Color'''
    print(colored(card.value_card(), color=card.color))


    """ def check_valid_move(self, user_input: str, player:Player):
        ''' This function determines the input of the Game cycle whether a card will be put into the card stack or a card will be drawn from deck'''
        if user_input == "DRAW":
            self.draw_from_deck(player)
            return None
        else :
            card = user_input
            while not player.check_card_in_hand(card, self.get_top_card()):
                print("You can't play that Card. Check Input")
                card = input("Type the card you want to play: [format:number/name - color] :")
                while not player.check_card_in_hand(card, self.get_top_card()):
                    card = input("Incorrect ! . Type the card you want to play: [format:number/name - color] :")
            return player.remove_card(card) """
    