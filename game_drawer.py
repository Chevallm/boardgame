import pygame
from pygame.locals import *
from pytmx import *

from game import Game


class GameDrawer:
    def __init__(self, game: Game, pygame: pygame, screen: pygame.Surface) -> None:
        self.game = game
        self.pygame = pygame
        self.screen = screen
        self.hovered_tile = None

    def draw(self):
        self.draw_board()
        self.draw_players()
        self.draw_hovered_tile()

    def draw_board(self):
        for layer in self.game.board.layers:
            for x, y, img in layer.tiles():
                self.screen.blit(img, (x*16, y*16))

    def draw_players(self):
        for player in self.game.players:
            self.screen.blit(player.sprite_bottom[0], (player.x*16, player.y*16))

    def draw_hovered_tile(self):
        if self.hovered_tile == None:
            return
        tile_x, tile_y = self.hovered_tile
        player_x, player_y = (self.game.players[0].x, self.game.players[0].y)
        if player_x == tile_x and player_y == tile_y:
            return
        tile_gid = self.game.board.get_tile_gid(tile_x, tile_y, 0)
        if tile_gid > 0:
            s = pygame.Surface((16, 16))
            s.set_alpha(128)
            s.fill((255, 0, 0))
            self.screen.blit(s, (tile_x *16, tile_y * 16))
            #pygame.draw.rect(self.screen, (255, 0, 0, 200), (tile_x*16, tile_y*16, 16, 16))
