from player import Player
from helpers import *
import random 

class Game: 
    
    '''Game Class that represent the instance of the Game of uno that will have Players that have Cards'''
    def __init__(self, players) -> None:
        self.players=players
        self.turn = 0 #Actual Turn that will only be between the index of self.players
        self.num_turn = 0  # Total of turns
        self.deck = self.init_deck()    
        self.card_stack = [] #Stack of Cards used  

    
    def play(self):
        print("Game Started!")
        while self.check_win() != True:
            print(f"Turn Number: {self.num_turn}")
            player = self.player_on_turn()
            if self.get_top_card() != None:
                print(" Card on Top of Stack: ")
                colored_print(self.get_top_card())
                print("\n")
            player.print_hand()
            self.card_input(self.get_top_card(), player)
            clear() #Clears Terminal after each turn 
            self.next_turn()
        
    def check_win(self):
        for player in self.players:
            if len(player.hand) == 0:
                print(f"{player.name} wins the game. Congratulations!")
                return True
            else: 
                return False 
            
    def player_on_turn(self):
        player = self.players[self.turn]
        print (f"{player.name} it's your turn")
        return player
    
    def next_turn(self): 
        self.turn = (self.turn + 1) % len(self.players) # Next Turn 
        self.num_turn += 1 # Total of Turns + 1
    
    def draw_from_deck(self, player: Player):
        clear() #Clears Terminal after each turn 
        user_flag = True
        while len(self.deck) != 0 and user_flag:
            print("This is the card you drew. Will be added to your deck: ")
            drawable_card = self.deck[random.randint(0, len(self.deck) - 1)]
            colored_print(drawable_card)
            user_input = input("Do you want to draw another Card ?: [format: yes/no] ")
            while not self.check_valid_response(user_input):
                print("Invalid Response ")
                user_input = input("Do you want to draw another Card ?: [format: yes/no] ")
            if user_input == "no":
                print("No more cards will be drawn. End of your turn")
                user_flag = False
            player.hand.append(drawable_card)

    @classmethod 
    def create_deck(cls):
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
        for i in range(4):
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

    def init_deck(self):
        ''' Function that creates the deck, shuffles it, and distributes 7 cards to each player '''
        cards = self.create_deck()
        random.shuffle(cards)

        for player in self.players:
            player.hand = cards[:7]
            cards = cards[7:]

        return cards
    
    def get_top_card(self):
        if self.num_turn != 0:
            top = self.card_stack[-1]
            return top
        else :
            return None
    
    def check_valid_response(self, user_input):
        if user_input == "yes" or user_input == "no":
            return True
        else:
            return False
        
    def card_input(self, top_card: Card, player: Player):
        ''' Player Method that ask the Player to input a card from it's hand and check if it's valid to play or if it exist'''
        user_input = input("Type the card you want to play [format:number/name - color] or if you want to draw a crad type DRAW :")
        response = self.check_valid_move(user_input, player)
        if isinstance(response, Card):
            self.card_stack.append(response)

    
    def check_valid_move(self, user_input: str, player:Player):
        if user_input == "DRAW":
            self.draw_from_deck(player)
            return None
        else :
            while not player.check_card_in_hand(user_input, self.get_top_card()):
                print("You can't play that Card. Check Input")
                card = input("Type the card you want to play: [format:number/name - color] :")
                return player.remove_card(card)
            return player.remove_card(user_input)
            
    def print_card_stack(self):
        for c in self.card_stack:
            colored_print(c)

    


        
            
            
            
