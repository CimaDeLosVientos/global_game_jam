import pygame, os, random, time as tim
from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *

class Character(sprite.Sprite):
    def __init__(self, position):
        sprite.Sprite.__init__(self)
        #self.image = transform.scale(load_image("assets/sprites/game_player.png"), OBJECT_SURFACE)
        self.image = load_image("assets/sprites/game_player_left.png")
        self.x = position[0]
        self.y = position[1]
        self.rect = self.image.get_rect()
        self.rect.topleft = (TILE_MARGIN + self.x * TILE_WIDTH, TILE_MARGIN + self.y * TILE_HEIGHT)

    def on_draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, y, x):
        self.x += x
        self.y += y
        self.rect.topleft = (self.x * TILE_WIDTH, self.y * TILE_HEIGHT)

    def update(self, time):
        pass#print(self.x, self.y)

class Player(Character):
    def __init__(self, position):
        Character.__init__(self, position)
        #self.image = transform.scale(load_image("assets/sprites/game_player.png"), OBJECT_SURFACE)
        self.sprites = {
            "left": load_image("assets/sprites/game_player_left.png"),
            "right": load_image("assets/sprites/game_player_right.png")
        }
        self.image = self.sprites["right"] if position[0] < 6 else self.sprites["left"]
        self.rect = self.image.get_rect()
        self.rect.topleft = (TILE_MARGIN + self.x * TILE_WIDTH, TILE_MARGIN + self.y * TILE_HEIGHT)
        self.orientation = "down"


    def move(self, y, x):
        if x > 0:
            self.change_orientation("right")
        if x < 0:
            self.change_orientation("left")
        self.x += x
        self.y += y
        self.rect.topleft = (self.x * TILE_WIDTH, self.y * TILE_HEIGHT)

    def change_orientation(self, orientation):
        self.orientation = orientation
        self.image = self.sprites[orientation]

class Enemy(Character):
    def __init__(self, alert, position):
        Character.__init__(self, position)
        #self.image = transform.scale(load_image("assets/sprites/game_enemy.png"), OBJECT_SURFACE)
        self.image = load_image("assets/sprites/game_enemy.png") if alert < 10 else load_image("assets/sprites/game_enemy_big.png")
        self.rect = self.image.get_rect()
        self.rect.center = (TILE_MARGIN + self.x * TILE_WIDTH + TILE_WIDTH / 2, TILE_MARGIN + self.y * TILE_HEIGHT + TILE_HEIGHT / 2)
        self.alert = alert

    def move(self, board, target):
        x, y = self.get_decision(board, target)
        self.x += x
        self.y += y
        self.rect.center = (self.x * TILE_WIDTH + TILE_WIDTH / 2, self.y * TILE_HEIGHT + TILE_HEIGHT / 2)

    def get_decision(self, board, target):
        x_delta = target[0] - self.x
        y_delta = target[1] - self.y
        if (abs(x_delta) + abs(y_delta)) == 0:
            return (0,0)
        if (self.alert**2 > (x_delta**2 + y_delta**2)):  # In range
            if abs(x_delta) > abs(y_delta):
                x_delta = int(x_delta / abs(x_delta))
                y_delta = 0
            else:
                x_delta = 0
                y_delta = int(y_delta / abs(y_delta))
        else:
            x_delta, y_delta = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
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