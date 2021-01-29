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
        self.rect.topleft = (TILE_MARGIN + self.x * TILE_WIDTH, TILE_MARGIN + self.y * TILE_HEIGHT)
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

    def move(self, board, target):
        x, y = self.get_decision(board, target)
        super().move(y, x)

    def get_decision(self, board, target):
        x_delta = target[0] - self.x
        y_delta = target[1] - self.y
        if abs(x_delta) > abs(y_delta):
            x_delta = int(x_delta / abs(x_delta))
            y_delta = 0
        else:
            x_delta = 0
            y_delta = int(y_delta / abs(y_delta))
        movement = (x_delta, y_delta)
        if self.can_move(board, movement):
            return movement
        else:
            return self.plan_b(board, movement)

    def plan_b(self, board, fail_movement):
        movement = (-fail_movement[1], fail_movement[0])
        if self.can_move(board, movement):
            return movement
        else:
            return self.plan_b(board, movement)

    def can_move(self, board, movement):
        target_tile_position = (self.y + movement[1], self.x + movement[0])
        if (target_tile_position[0] >= 0 and
            target_tile_position[1] >= 0 and
            target_tile_position[0] < len(board) and
            target_tile_position[1] < len(board[0]) and
            board[target_tile_position[0]][target_tile_position[1]].transitable and
            not board[target_tile_position[0]][target_tile_position[1]].hiding_place and
            not board[target_tile_position[0]][target_tile_position[1]].under_enemy):
            return True
        else:
            return False