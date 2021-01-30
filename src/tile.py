import pygame, os, random, time as tim
from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *

""" 
Tile_types:
0 - empthy
1 - obstacle_1
2 - obstacle_2
3 - obstacle_3
4 - obstacle_4
5 - shelter_1
6 - shelter_2
7 - fairy
8 - book_page

"""
class Tile(sprite.Sprite):
    def __init__(self, tile_type, position):
        sprite.Sprite.__init__(self)
        #self.image = transform.scale(load_image("assets/sprites/obstacle.png"), OBJECT_SURFACE)
        self.image = None

        self.transitable = True
        self.hiding_place = False

        if 0 < tile_type < 5:
            self.image = load_image("assets/sprites/obstacle_{tile_type}.png".format(tile_type=tile_type))
            self.transitable = False
        elif 4 < tile_type < 7:
            self.image = load_image("assets/sprites/shelter_{tile_type}.png".format(tile_type=tile_type-4))
            self.hiding_place = True
        elif tile_type == 7:
            self.image = load_image("assets/sprites/game_fairy.png")
            self.hiding_place = True
        elif tile_type == 8:
            self.image = load_image("assets/sprites/game_book.png")
            self.hiding_place = True
        self.x = position[0]
        self.y = position[1]
        if self.image:
            self.rect = self.image.get_rect()
            self.rect.center = (
                TILE_MARGIN + self.x * TILE_WIDTH + TILE_WIDTH / 2,
                TILE_MARGIN + self.y * TILE_HEIGHT + TILE_HEIGHT / 2
            )
        #self.pulsable = False  # values = { "up", "down", "right", "left"}
        self.under_player = False
        self.under_enemy = False

    def pressed(self, mouse_position):
        if self.rect.collidepoint(mouse_position) and self.pulsable:
            return self.pulsable

    def update(self, time):
        pass

    def on_draw(self, screen):
        if self.image:            
            screen.blit(self.image, self.rect)