import pygame, os, random, time as tim
from pygame.locals import *
from .scene import Scene
from .helpers import *
from .parameters import *

class MainMenu(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.next = None
        self.music = "assets/music/Phillip_Gross_-_02_-_Neon_Twin.mp3"
        self.background = load_image("assets/images/scenes/main_menu.png")

        # Play button
        self.play_button = load_image("assets/images/buttons/play_button.png")
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = PLAY_BUTTON
        
        # How to play button
        self.how_play_button = load_image("assets/images/buttons/how_play_button.png")
        self.how_play_button_rect = self.how_play_button.get_rect()
        self.how_play_button_rect.center = HOW_TO_PLAY_BUTTON

        # Credits button
        self.credits_button = load_image("assets/images/buttons/credits_button.png")
        self.credits_button_rect = self.credits_button.get_rect()
        self.credits_button_rect.center = CREDITS_BUTTON

        self.mouse_state = 1 # Up


    def load(self, data):
        self.__init__()
        if not pygame.mixer.music.get_busy():
            load_music(self.music)
            pygame.mixer.music.play(-1)


    def on_event(self, time, event):
        mouse_press = pygame.mouse.get_pressed()[0]
        if (mouse_press and self.mouse_state == 1):
            self.mouse_state = 0
        if (not mouse_press and self.mouse_state == 0):
            if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
                self.next = "play_menu"
            if self.how_play_button_rect.collidepoint(pygame.mouse.get_pos()):
                self.next = "how_to_play"
            if self.credits_button_rect.collidepoint(pygame.mouse.get_pos()):
                self.next = "credits"
            self.mouse_state = 1


    def on_update(self, time):
        pass


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo

        # Scene
        screen.blit(self.background, self.background.get_rect())
        
        # Buttons
        screen.blit(self.play_button, self.play_button_rect)
        screen.blit(self.how_play_button, self.how_play_button_rect)
        screen.blit(self.credits_button, self.credits_button_rect)



    def finish(self, data):
        pass
