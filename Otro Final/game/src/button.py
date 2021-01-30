import pygame, os, random, time as tim
from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *


class Button(sprite.Sprite):
    def __init__(self, active, inactive, hover, position, on_click):
        sprite.Sprite.__init__(self)
        self.image = active
        self.active = active
        self.inactive = inactive
        self.hover = hover
        self.turn_on = False
        self.x = position[0]
        self.y = position[1]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.on_click = on_click

    def on_hover(self, state):
        if state and self.turn_on:
            self.image = self.hover
        else:
            self.image = self.active if self.turn_on else self.inactive    

    def on_draw(self, screen):
        screen.blit(self.image, self.rect)

    def switch(self, state):
        self.turn_on = state
        self.image = self.active if self.turn_on else self.inactive





class ButtonUp(Button):
    def __init__(self, position, on_click):
        super(ButtonUp, self).__init__(
            active = load_image("assets/sprites/up_on.png"),
            inactive = load_image("assets/sprites/up_off.png"),
            hover = load_image("assets/sprites/over_up.png"),
            position = position,
            on_click = on_click)

class ButtonLeft(Button):
    def __init__(self, position, on_click):
        super(ButtonLeft, self).__init__(
            active = load_image("assets/sprites/left_on.png"),
            inactive = load_image("assets/sprites/left_off.png"),
            hover = load_image("assets/sprites/over_left.png"),
            position = position,
            on_click = on_click)

class ButtonRight(Button):
    def __init__(self, position, on_click):
        super(ButtonRight, self).__init__(
            active = load_image("assets/sprites/right_on.png"),
            inactive = load_image("assets/sprites/right_off.png"),
            hover = load_image("assets/sprites/over_right.png"),
            position = position,
            on_click = on_click)

class ButtonDown(Button):
    def __init__(self, position, on_click):
        super(ButtonDown, self).__init__(
            active = load_image("assets/sprites/down_on.png"),
            inactive = load_image("assets/sprites/down_off.png"),
            hover = load_image("assets/sprites/over_down.png"),
            position = position,
            on_click = on_click)

class ButtonWait(Button):
    def __init__(self, position, on_click):
        super(ButtonWait, self).__init__(
            active = load_image("assets/sprites/wait_on.png"),
            inactive = load_image("assets/sprites/wait_off.png"),
            hover = load_image("assets/sprites/over_wait.png"),
            position = position,
            on_click = on_click)