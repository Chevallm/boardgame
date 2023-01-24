import time
from operator import indexOf
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
        for layer in self.game.board.visible_layers:
            print(layer.name, layer.visible)
            for x, y, img in layer.tiles():
                self.screen.blit(img, (x*32, y*32))
        #animation_start_time = time.time()
        #for gid, tile_properties in self.game.board.tile_properties.items():
            # iterate over the frames of the animation
            # if there is no animation, this list will be empty
            #if 'animation' in tile_properties:
                #animation = tile_properties['animation']
                #duration = animation.duration
                #elapsed_time = time.time() - animation_start_time
                #current_frame = int(elapsed_time / duration) % len(animation)
                #image = self.game.board.get_tile_image_by_gid(gid + current_frame)
                #self.screen.blit(image, (tile_properties.))

    def draw_players(self):
        for player in self.game.players:
            self.screen.blit(player.sprite_bottom[0], (player.x * 32, player.y * 32))

    def draw_hovered_tile(self):
        if self.hovered_tile == None:
            return
        tile_x, tile_y = self.hovered_tile
        player_x, player_y = (self.game.players[0].x, self.game.players[0].y)
        if player_x == tile_x and player_y == tile_y:
            return
        collision_layer = self.game.board.get_layer_by_name('collision')
        collision_layer_index = indexOf(self.game.board, collision_layer)
        tile_gid = self.game.board.get_tile_gid(tile_x, tile_y, collision_layer_index)
        if tile_gid == 0:
            s = pygame.Surface((32, 32))
            s.set_alpha(128)
            s.fill((255, 0, 0))
            self.screen.blit(s, (tile_x * 32, tile_y * 32))
