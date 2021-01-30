import pygame, os, random, time as tim
from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *
from .tile import Tile

class Board(sprite.Sprite):
    def __init__(self, raw_board, player, enemies, goal_pos, position):
        sprite.Sprite.__init__(self)
        self.background = load_image("assets/sprites/play_area.png")
        self.grid = load_image("assets/sprites/grid.png")

        self.x = position[0]
        self.y = position[1]
        self.background_rect = self.background.get_rect()
        self.background_rect.topleft = (TILE_MARGIN + position[0], TILE_MARGIN + position[1])
        self.grid_rect = self.grid.get_rect()
        self.grid_rect.topleft = position
        self.goal_pos = goal_pos
        self.player = player
        self.enemies = enemies
        self.transiting = False  # Maybe external
        self.tiles = self.get_tiles(raw_board)
        self.set_unders()
        self.tiles_dimensions = (len(self.tiles), len(self.tiles[0]))  # Index like a matrix (x=height, y = width)

        # Hiding control. If the hide time change for diferents tiles, this function maybe must move on to Tile
        self.shelter_expiration = SHELTER_EXPIRATION_TIME


    def get_tiles(self, raw_board):
        return [
            [
                Tile(raw_tile, (tile_index, row_index))
                for tile_index, raw_tile in enumerate(row)
            ]
            for row_index, row in enumerate(raw_board)
        ]

    def set_unders(self):
        self.tiles[self.player.y][self.player.x].under_player = True
        for enemy in self.enemies:
            self.tiles[enemy.y][enemy.x].under_enemy = True

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

    def move_enemies(self):
        for enemy in self.enemies:
            self.tiles[enemy.y][enemy.x].under_enemy = False
            if self.tiles[self.player.y][self.player.x].hiding_place:
                enemy.move(self.tiles, (random.randrange(0, self.tiles_dimensions[1]), random.randrange(0, self.tiles_dimensions[0])))
                self.shelter_expiration -= 1
            else:
                enemy.move(self.tiles, (self.player.x, self.player.y))
                self.shelter_expiration = SHELTER_EXPIRATION_TIME
            self.tiles[enemy.y][enemy.x].under_enemy = True

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
            "wait": self.shelter_expiration > 0
        }


    def update(self, time):
        player_pos = (self.player.x, self.player.y)
        if player_pos == self.goal_pos:
            print("PLAYER WINS")
        for enemy in self.enemies:
            if (enemy.x, enemy.y) == player_pos:
                print("PLAYER LOSES")

    def on_draw(self, screen):
        screen.blit(self.background, self.background_rect)
        screen.blit(self.grid, self.grid_rect)
        board_screen = pygame.Surface((TILE_WIDTH * len(self.tiles[0]), TILE_HEIGHT * len(self.tiles))).convert_alpha()
        board_screen.fill((0,0,0,0))
        board_screen_rect = board_screen.get_rect()
        board_screen_rect.topleft = self.grid_rect.topleft
        
        self.player.on_draw(board_screen)
        self.enemies.draw(board_screen)
        for tile_row in self.tiles:
            for tile in tile_row:
                tile.on_draw(board_screen)

        screen.blit(board_screen, board_screen_rect)