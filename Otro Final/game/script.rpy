﻿# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define elder = Character("Gran Sabio")
define girl = Character("GIRL")
define fairy = Character("HADA")
define evil = Character("EVIL")


# El juego comienza aquí.
init -1 python:
    from src.game import Game
    from src.parameters import MINIGAMES_DATA

    data = {}
    scenes = {
        "init" : Game(MINIGAMES_DATA["3"])
    }


label test_zone:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene game_menu
    show logo x p at center0
    narrator "Has creado un nuevo juego Ren'Py."
    show logo j at center1
    narrator "Has creado un nuevo juego Ren'Py."
    show logo x p k at center2
    narrator "Has creado un nuevo juego Ren'Py."
    show logo at center3
    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.
    python:
        director = Director(scenes, data)
        ui.add(director)
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)
        ui.remove(director)
    narrator "Has creado un nuevo juego Ren'Py."
    jump cosa
    menu:
        "{b}patata{\b}":
            e"jajajaj"
        "20}lllasd":
            e"ca culo pedo pis"

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"


    show eileen happy

    # Presenta las líneas del diálogo.

    e "Has creado un nuevo juego Ren'Py."

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"
    # Finaliza el juego:
label start:
    #jump sc_001_story_telling
    jump test_zone


    return
