import pygame, os, random, time as tim
from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *

class Character(sprite.Sprite):
    def __init__(self, position):
        sprite.Sprite.__init__(self)
        #self.image = transform.scale(load_image("assets/sprites/game_player.png"), OBJECT_SURFACE)
        self.image = load_image("assets/sprites/game_player.png")
        self.x = position[0]
        self.y = position[1]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * TILE_WIDTH, self.y * TILE_HEIGHT)
        self.orientation = "down"

    def on_draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, y, x):
        self.x += x
        self.y += y
        self.rect.topleft = (self.x * TILE_WIDTH, self.y * TILE_HEIGHT)
        # change orientation

    def change_orientation(self, orientation):
        raise NotImplementedError
        self.orientation = orientation
        self.image = self.sprite_shift[orientation]

    def update(self, time):
        pass#print(self.x, self.y)

class Enemy(Character):
    def __init__(self, position):
        Character.__init__(self, position)
        #self.image = transform.scale(load_image("assets/sprites/game_enemy.png"), OBJECT_SURFACE)
        self.image = load_image("assets/sprites/game_enemy.png")

    def get_decision(self, board):
        pass