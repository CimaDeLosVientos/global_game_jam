import pygame, os, random, time as tim
from pygame.locals import *
from .scene import Scene
from .helpers import *
from .parameters import *
from .board import Board
from .character import Character, Enemy, Player
from .panel import Panel

class Game(Scene):
    def __init__(self, data):
        Scene.__init__(self)
        self.next = None
        self.background = load_image("assets/sprites/game_background.png")
        self.player = Player(data["player_pos"])
        self.enemies = pygame.sprite.Group()
        self.enemies.add([
            Enemy(enemy["alert"], enemy["pos"])
            for enemy in data["enemies"].values()
        ])
        self.board = Board(data["raw_board"], self.player, self.enemies, data["goal"], GAME_FIELD_POSITION_TL)
        self.panel = Panel(PANEL_POSITION)
        self.panel.set_buttons_states(self.board.get_button_states())


    def load(self, data):
        return
        self.__init__()


    def on_event(self, time, event):
        self.panel.on_event(time, event)


    def on_update(self, time):
        self.player.update(time)
        self.enemies.update(time)
        self.board.update(time)
        movement = self.panel.update(time)
        #print(movement)
        if movement:
            self.board.move_player(movement)
            # move enemies
            self.board.move_enemies()
            self.panel.set_buttons_states(self.board.get_button_states())
            



    def on_draw(self, screen):
        # Scene
        screen.blit(self.background, self.background.get_rect())
        
        self.board.on_draw(screen)
        self.panel.on_draw(screen)



    def finish(self, data):
        pass
