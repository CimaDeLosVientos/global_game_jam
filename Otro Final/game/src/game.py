import pygame, os, random, time as tim
from pygame.locals import *
from .scene import Scene
from .helpers import *
from .parameters import *
from .board import Board
from .character import Character, Enemy
from .panel import Panel

class Game(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.next = None
        self.background = load_image("assets/sprites/game_background.png")
        self.player = Character((2,2))
        self.enemies = pygame.sprite.Group()
        self.enemies.add([Enemy((5,5)), Enemy((5,6))])
        self.board = Board(RAW_BOARD_0, self.player, self.enemies, GAME_FIELD_POSITION_TL)
        self.panel = Panel(PANEL_POSITION)
        self.panel.set_buttons_states(self.board.get_button_states())




    def load(self, data):
        self.__init__()


    def on_event(self, time, event):
        self.panel.on_event(time, event)


    def on_update(self, time):
        self.player.update(time)
        self.enemies.update(time)
        result = self.board.update(time)
        if result:
            return result
        movement = self.panel.update(time)
        if movement:
            self.board.move_player(movement)
            # move enemies
            self.board.move_enemies()
            self.panel.set_buttons_states(self.board.get_button_states())
            



    def on_draw(self, screen):
        # Scene
        screen.blit(self.background, self.background.get_rect().topleft)
        
        self.board.on_draw(screen)
        self.panel.on_draw(screen)



    def finish(self, data):
        pass
