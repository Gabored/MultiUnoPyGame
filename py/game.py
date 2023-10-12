from player import Player

class Game: 
    '''Game Class that represent the instance of the Game of uno that will have Players that have Cards'''
    def __init__(self, players: Player) -> None:
        self.players=players
        self.topOfStack = None
    
    def play(self):
        print("Game Started!")
        for p in self.players:
            p.card_input(self.topOfStack)
            p.print_hand()
