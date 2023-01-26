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
        self.board = load_pygame("./tiled/map2.tmx")

    def init_players(self):
        self.players.append(Player('human', 'human', 3, 3))
        self.players.append(Player('magician', 'magician', 4, 3))
        self.players.append(Player('archer', 'archer', 5, 3))

    def move_player_to(self, player, x, y):
        if (x > 0 or x < self.board.width) or (y > 0 or y < self.board.height):
            player.move_to(x, y)
