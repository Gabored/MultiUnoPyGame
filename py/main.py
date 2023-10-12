from helpers import create_deck
import random
from player import Player



def init_deck():
    ''' Example function that creates the deck , shuffles it and returns 4 card lists '''
    cards= create_deck()
    random.shuffle(cards) #In Place Shuffle
    return cards[0:13], cards[13:26], cards[26:39], cards[39:52]


# Starting Game with 4 players 
h1 , h2, h3, h4 = init_deck()
player1 = Player("1", h1)
player2 = Player("2", h2)
player3 = Player("3", h3)
player4 = Player("4", h4)

print("\n")
print(player1.hand)
print("\n")
print(player2.hand)
print("\n")
print(player3.hand)
print("\n")
print(player4.hand)






