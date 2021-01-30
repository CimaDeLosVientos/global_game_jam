import pygame, os, random, time as tim
from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *

class Tile(sprite.Sprite):
    def __init__(self, tile_type, position):
        sprite.Sprite.__init__(self)
        #self.image = transform.scale(load_image("assets/sprites/obstacle.png"), OBJECT_SURFACE)
        self.image = None
        if tile_type == 1:
            self.image = load_image("assets/sprites/obstacle_big.png")
        if tile_type == 5:
            self.image = load_image("assets/sprites/shelter.png")
        self.x = position[0]
        self.y = position[1]
        if self.image:
            self.rect = self.image.get_rect()
            self.rect.center = (
                TILE_MARGIN + self.x * TILE_WIDTH + TILE_WIDTH / 2,
                TILE_MARGIN + self.y * TILE_HEIGHT + TILE_HEIGHT / 2
            )
        self.transitable = True if tile_type != 1 else False
        #self.pulsable = False  # values = { "up", "down", "right", "left"}
        self.hiding_place = True if tile_type == 5 else False
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