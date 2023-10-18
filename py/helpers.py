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
