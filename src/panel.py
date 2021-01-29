import pygame, os, random, time as tim
from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *
from .button import ButtonUp, ButtonLeft, ButtonRight, ButtonDown, ButtonWait

class Panel(sprite.Sprite):
    def __init__(self, position):
        sprite.Sprite.__init__(self)
        self.background = load_image("assets/sprites/interface_panel.png")
        self.x = position[0]
        self.y = position[1]
        self.background_rect = self.background.get_rect()
        self.background_rect.topleft = position
        self.buttons = {
            "up": ButtonUp(POSITION_BUTTON_UP, lambda: self.set_movement("up")),
            "left": ButtonLeft(POSITION_BUTTON_LEFT, lambda: self.set_movement("left")),
            "right": ButtonRight(POSITION_BUTTON_RIGHT, lambda: self.set_movement("right")),
            "down": ButtonDown(POSITION_BUTTON_DOWN, lambda: self.set_movement("down")),
            "wait": ButtonWait(POSITION_BUTTON_WAIT, lambda: self.set_movement("wait"))
        }
        self.buttons_group = pygame.sprite.Group()
        self.buttons_group.add(self.buttons.values())

        self.mouse_state = 1 # Up

        self.mouse_press = False
        self.mouse_pos = (0,0)


        self.order = None


    def on_event(self, time, event):
        #mouse_press = pygame.mouse.get_pressed()[0]
        #mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            self.mouse_press = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_press = True
        if event.type == pygame.MOUSEMOTION:
            self.mouse_pos = event.pos
        for button in self.buttons_group:
            print(button.rect)
            print(self.mouse_pos[0], self.x, self.mouse_pos[1], self.y)
            if button.rect.collidepoint((self.mouse_pos[0] - self.x, self.mouse_pos[1] - self.y)):
                button.on_hover(True)
            else:
                button.on_hover(False)
        if (self.mouse_press and self.mouse_state == 1):
            self.mouse_state = 0
        if (not self.mouse_press and self.mouse_state == 0):
            for button in self.buttons_group:
                if button.rect.collidepoint((self.mouse_pos[0] - self.x, self.mouse_pos[1] - self.y)):
                    button.on_click()
            self.mouse_state = 1


    def update(self, time):
        if self.order:
            aux = self.order
            self.order = None
            return aux


    def on_draw(self, screen):
        aux_background = self.background.copy()  # Quitando esto sale un efecto de fade chulo
        self.buttons_group.draw(aux_background)
        screen.blit(aux_background, self.background_rect)


    def set_buttons_states(self, states):
        for button_name, state in states.items():
            self.buttons[button_name].switch(state)

    def set_movement(self, direction):
        if self.buttons[direction].turn_on:
            self.order = direction