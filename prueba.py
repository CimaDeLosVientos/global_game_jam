import pygame_sdl2 as pygame
import os, random, time as tim
from pygame.locals import *

print("caca")
pygame.init()

screen = pygame.display.set_mode([700, 700])
#screen = pygame.display.set_mode([WIDTH, HEIGHT], flags = pygame.FULLSCREEN)



# Variables
clock = pygame.time.Clock()
quit_flag = False

#Options
pygame.key.set_repeat(10)

i = 0
while not quit_flag:
    time = clock.tick(60) # Must be in loop
    # Eventos de Salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()

        # detecta eventos
        #current_scene.on_event(time, event)
    # actualiza la escena
    if i % 100 < 50:
        screen.fill((0, 0, 0))
    else:
        screen.fill((0, 100, 50))
    i = i+1
    pygame.display.flip()
