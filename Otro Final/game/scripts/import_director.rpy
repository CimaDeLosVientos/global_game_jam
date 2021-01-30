init -1 python:

    # need some imports
    import random
    import math
    import pygame
    import time

    from src.parameters import *
    pygame.key.set_repeat(10)
    class Director(renpy.Displayable):

        #Debe sobreescribirse el constructor
        def __init__(self, scenes, data, **kwargs):
            super(Director, self).__init__(**kwargs)
     

            self.height = WIDTH
            self.width = HEIGHT
            self.clock = pygame.time.Clock()
            #Para calcular tiempos
            self.oldst = None
            self.result = None # To end variable
            self.stuck = True

            # Para control del juego
            self.scenes = scenes
            self.current_scene = self.scenes["init"]
            self.data = data
            self.current_scene = self.scenes["init"]
            self.current_scene.load(self.data) # Se le manda el diccionario de datos para que se configure.




        '''
        Renderiza el objeto en la escena.
        Heredado de renpy.Displayable
        width, height
            The amount of space available to this displayable, in pixels.
        st
            A float, the shown timebase, in seconds. The shown timebase 
            begins when this displayable is first shown on the screen.
        at
            A float, the animation timebase, in seconds. The animation timebase begins when 
            an image with the same tag was shown, without being hidden.
            (When the displayable is shown without a tag, this is the same as 
                the shown timebase.) '''
        def render(self, width, height, st, at):
            time = self.clock.tick(60)
            screen = renpy.Render(self.width, self.height)
            # Para poder saber el tiempo
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st
            # actualiza la escena
            result = self.current_scene.on_update(time)
            if result:
                self.result = result

            # dibuja la pantalla
            self.current_scene.on_draw(screen)


            if self.current_scene.next:
                self.change_scene()

            renpy.redraw(self, 0)
            return screen



        def change_scene(self):
            self.current_scene.finish(self.data) # Se le manda el diccionario de datos para que lo actualice.
            self.current_scene = self.scenes[self.current_scene.next]
            self.current_scene.load(self.data) # Se le manda el diccionario de datos para que se configure.



        '''
        ev
            An event object
        x, y
            The x and y coordinates of the event, relative to the upper-left 
            corner of the displayable. These should be used in preference to 
            position information found in the pygame event objects.
        st
            A float, the shown timebase, in seconds.
        An event is generated at the start of each interaction, and renpy.timeout() 
        can be used to cause another event to occur.'''
        def event(self, ev, x, y, st):
            dtime = st - self.oldst
            time = self.clock.tick(60)
            self.current_scene.on_event(time, (ev, x, y))

            result = self.current_scene.on_update(time)
            if result:  # Quitable
                self.result = result

            if self.result:
                return self.result
            else:
                raise renpy.IgnoreEvent()

        '''
        Similar a update de pygame'''
        def per_interact(self):
            pass

        '''
        Devuelve la lista de hijos '''
        def visit(self):
            return [] 

    print("Cargado")