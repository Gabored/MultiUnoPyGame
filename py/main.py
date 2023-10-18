

from player import Player
from game import Game





# Starting Game with 4 players 

player1 = Player("Lucas")
player2 = Player("Sophie")
player3 = Player("Paul")
player4 = Player("Will")

# Play Game 

table = Game(players=[player1, player2, player3, player4])
table.play()







