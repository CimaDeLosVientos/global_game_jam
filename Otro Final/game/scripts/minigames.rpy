init -1 python:
    from src.game import Game
    from src.parameters import MINIGAMES_DATA

    scenes_1 = {
        "init" : Game(MINIGAMES_DATA["1"])
    }
    scenes_2 = {
        "init" : Game(MINIGAMES_DATA["2"])
    }
    scenes_3 = {
        "init" : Game(MINIGAMES_DATA["3"])
    }
    scenes_4 = {
        "init" : Game(MINIGAMES_DATA["4"])
    }
    scenes_5 = {
        "init" : Game(MINIGAMES_DATA["5"])
    }


label minigame_1:
    pause (1)
    call HIDE from _call_HIDE
    window hide
    python:
        director = Director(scenes_1, MINIGAMES_DATA["1"])
        ui.add(director)
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)
        ui.remove(director)
        director = None

    if winner == "True":
        $ renpy.block_rollback()
        jump sc_005_before_book
    else:
        jump dead_end

label minigame_2:
    pause (1)
    call HIDE from _call_HIDE_1
    window hide
    python:
        director = Director(scenes_2, MINIGAMES_DATA["2"])
        ui.add(director)
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)
        ui.remove(director)
        director = None

    if winner == "True":
        $ renpy.block_rollback()
        jump sc_006_book_enemy
    else:
        jump dead_end

label minigame_3:
    pause (1)
    #call HIDE from _call_HIDE_2
    #window hide
    python:
        director = Director(scenes_3, MINIGAMES_DATA["3"])
        ui.add(director)
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)
        ui.remove(director)
        director = None

    if winner == "True":
        $ renpy.block_rollback()
        jump sc_007_reading_conversation
    else:
        jump dead_end

label minigame_4:
    pause (1)
    call HIDE from _call_HIDE_3
    window hide
    python:
        director = Director(scenes_4, MINIGAMES_DATA["4"])
        ui.add(director)
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)
        ui.remove(director)
        director = None

    if winner == "True":
        $ renpy.block_rollback()
        jump sc_008_running_reading
    else:
        jump dead_end

label minigame_5:
    pause (1)
    call HIDE from _call_HIDE_4
    window hide
    python:
        director = Director(scenes_5, MINIGAMES_DATA["5"])
        ui.add(director)
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)
        ui.remove(director)
        director = None

    if winner == "True":
        $ renpy.block_rollback()
        jump sc_009_panic_moment
    else:
        jump dead_end