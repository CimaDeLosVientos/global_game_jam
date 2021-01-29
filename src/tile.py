import pygame, os, random, time as tim
from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *

class Tile(sprite.Sprite):
    def __init__(self, tile_type, position):
        sprite.Sprite.__init__(self)
        #self.image = transform.scale(load_image("assets/sprites/obstacle.png"), OBJECT_SURFACE)
        self.image = load_image("assets/sprites/obstacle.png") if tile_type != 0 else None
        self.x = position[0]
        self.y = position[1]
        if self.image:
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x * TILE_WIDTH, self.y * TILE_HEIGHT)
        self.transitable = True if tile_type == 0 else False
        self.pulsable = False  # values = { "up", "down", "right", "left"}
        self.hiding_place = False
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