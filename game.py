from pytmx import *

from player import Player

class Game:
    
    def __init__(self) -> None:
        self.board = []
        self.players = []
        self.monsters = []
        self.init_board()
        self.init_players()

    def init_board(self):
        self.board = load_pygame("./tiled/map1.tmx")

    def init_players(self):
        self.players.append(Player('human', 'human2', 4, 3))


