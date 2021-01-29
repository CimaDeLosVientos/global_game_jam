import pygame, os, random, time as tim
from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *
from .tile import Tile

class Board(sprite.Sprite):
    def __init__(self, raw_board, player, enemies, position):
        sprite.Sprite.__init__(self)
        self.background = load_image("assets/sprites/play_area.png")
        self.grid = load_image("assets/sprites/grid.png")

        self.x = position[0]
        self.y = position[1]
        self.background_rect = self.background.get_rect()
        self.background_rect.center = position
        self.grid_rect = self.grid.get_rect()
        self.grid_rect.center = position
        self.player = player
        self.enemies = enemies
        self.transiting = False  # Maybe external
        self.tiles = self.get_tiles(raw_board)
        self.tiles_dimensions = (len(self.tiles), len(self.tiles[0]))

    def get_tiles(self, raw_board):
        return [
            [
                Tile(raw_tile, (tile_index, row_index))
                for tile_index, raw_tile in enumerate(row)
            ]
            for row_index, row in enumerate(raw_board)
        ]

    def move_player(self, movement):
        if movement != "wait":
            self.tiles[self.player.y][self.player.x].under_player = False
            if movement == "up":
                self.tiles[self.player.y - 1][self.player.x].under_player = True
                self.player.move(-1,0)
            if movement == "left":
                self.tiles[self.player.y][self.player.x - 1].under_player = True
                self.player.move(0,-1)
            if movement == "right":
                self.tiles[self.player.y][self.player.x + 1].under_player = True
                self.player.move(0,1)
            if movement == "down":
                self.tiles[self.player.y + 1][self.player.x].under_player = True
                self.player.move(+1,0)
        return self.get_button_states()

    def get_button_states(self):
        return {
            "up": (
                self.player.y > 0 and
                self.tiles[self.player.y-1][self.player.x].transitable
            ),
            "left": (
                self.player.x > 0 and
                self.tiles[self.player.y][self.player.x-1].transitable
            ),
            "right": (
                self.player.x < self.tiles_dimensions[1]-1 and
                self.tiles[self.player.y][self.player.x+1].transitable
            ),
            "down": (
                self.player.y < self.tiles_dimensions[0]-1 and
                self.tiles[self.player.y+1][self.player.x].transitable
            ),
            "wait": True
        }


    def update(self, time):
        pass

    def on_draw(self, screen):
        screen.blit(self.background, self.background_rect)
        screen.blit(self.grid, self.grid_rect)
        board_screen = pygame.Surface((TILE_WIDTH * len(self.tiles[0]), TILE_HEIGHT * len(self.tiles))).convert_alpha()
        board_screen.fill((0,0,0,0))
        board_screen_rect = board_screen.get_rect()
        board_screen_rect.topleft = self.grid_rect.topleft
        for tile_row in self.tiles:
            for tile in tile_row:
                tile.on_draw(board_screen)
        self.player.on_draw(board_screen)
        self.enemies.draw(board_screen)

        screen.blit(board_screen, board_screen_rect)