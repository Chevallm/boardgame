from game_drawer import GameDrawer
import pygame
from pygame.locals import *

from game import Game
 
class App:
    def __init__(self):
        self._running = True
        self._screen = None
        self.size = self.weight, self.height = 40*32, 60*32
 
    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.game = Game()
        self.game_drawer = GameDrawer(self.game, pygame, self._screen)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                self.game.players[0].y -= 1
            if event.key == pygame.K_DOWN:
                self.game.players[0].y += 1
            if event.key == pygame.K_LEFT:
                self.game.players[0].x -= 1
            if event.key == pygame.K_RIGHT:
                self.game.players[0].x += 1


        if event.type == pygame.MOUSEMOTION:
            tile_x, tile_y = pygame.mouse.get_pos()
            tile_x, tile_y = tile_x // 32, tile_y // 32
            tile = self.game.board.get_tile_gid(tile_x, tile_y, 0)
            self.game_drawer.hovered_tile = tile_x, tile_y

        if event.type == pygame.MOUSEBUTTONDOWN:
            tile_x, tile_y = pygame.mouse.get_pos()
            tile_x, tile_y = tile_x // 32, tile_y // 32
            tile = self.game.board.get_tile_gid(tile_x, tile_y, 0)
            if tile == 0: # not floor
                pass
            
            else:
                self.game.players[0].x = tile_x
                self.game.players[0].y = tile_y
        

    def on_loop(self):
        pass

    def on_render(self):
        self._screen.fill((0, 0, 0))
        self.game_drawer.draw()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()