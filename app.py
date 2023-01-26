from operator import indexOf

import pygame

from game import Game
from game_drawer import GameDrawer


class App:
    def __init__(self):
        self.game_drawer = None
        self.game = None
        self._running = True
        self._screen = None
        self.size = self.weight, self.height = 30 * 32, 20 * 32

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
            pass

        if event.type == pygame.MOUSEMOTION:
            tile_x, tile_y = pygame.mouse.get_pos()
            tile_x, tile_y = tile_x // 32, tile_y // 32
            self.game_drawer.hovered_tile = tile_x, tile_y

        if event.type == pygame.MOUSEBUTTONDOWN:
            tile_x, tile_y = pygame.mouse.get_pos()
            tile_x, tile_y = tile_x // 32, tile_y // 32
            collision_layer = self.game.board.get_layer_by_name('collision')
            collision_layer_index = indexOf(self.game.board.layers, collision_layer)
            tile = self.game.board.get_tile_gid(tile_x, tile_y, collision_layer_index)
            can_move = tile is 0
            if can_move:
                self.game.move_player_to(self.game.players[1], tile_x, tile_y)

    def on_loop(self):
        pass

    def on_render(self):
        self._screen.fill((50, 50, 50))
        self.game_drawer.draw()
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
