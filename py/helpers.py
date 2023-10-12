from card import Card

def create_deck():
    ''' Creates Uno Deck accordint to original game instructions 
    8 Red cards – 0 to 9
    8 Blue cards – 0 to 9
    8 Green cards – 0 to 9
    8 Yellow cards – 0 to 9
    4 Skip cards – two cards of each color
    4 Reverse cards – two cards of each color
    4 Draw cards – two cards of each color
    4 Black cards – 4 wild cards and 4 Wild Draw 4 cards
    '''
    deck = []
    for i in range(2):
        for color in ["red", "green", "blue", "yellow"]:
            for number in range(1,10):
                deck.append( Card(color=color, number=number))
            for action in ["skip", "reverse", "+2"]:
                deck.append(Card (color=color, action=action))

    
        deck.append(Card(color= "black", action= "+4" ))
        deck.append(Card(color= "black", action= "+4" ))
        deck.append(Card(color= "black", action="wild"))
        deck.append(Card(color= "black", action="wild"))
    
    return deck 

def print_deck(deck: Card) -> None:
    '''Function that uses repr method of Card to print the deck in a legible form '''
    for card in deck:
        print(card.__repr__())
