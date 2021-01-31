# Display
WIDTH  = 1920
HEIGHT = 1080
#WIDTH  = 1280
#HEIGHT = 720

TILE_WIDTH = 75
TILE_HEIGHT = 75
TILE_MARGIN = 5



TILE_SURFACE = (TILE_WIDTH, TILE_HEIGHT)

PANEL_POSITION = (WIDTH - 302, 0)
GAME_FIELD_POSITION_TL = (300, 200)
PANEL_BUTTON_PADDING = 1712 - PANEL_POSITION[0] 
POSITION_BUTTON_UP = (PANEL_BUTTON_PADDING, 182)
POSITION_BUTTON_LEFT = (PANEL_BUTTON_PADDING, 336)
POSITION_BUTTON_RIGHT = (PANEL_BUTTON_PADDING, 490)
POSITION_BUTTON_DOWN = (PANEL_BUTTON_PADDING, 644)
POSITION_BUTTON_WAIT = (PANEL_BUTTON_PADDING, 798)


# Boards
RAW_BOARD_0 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,1,0,0,0,0,1,0],
    [0,0,5,0,0,0,0,1,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,0,1],
    [0,0,0,0,0,0,0,0,1,0,0,1,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,5,0,1,0,0,0,5,0,0],
    [0,0,0,0,0,1,0,0,0,5,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0]
]

RAW_BOARD_1 = [
    [0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,1,0,0,0,0,0,7],
    [0,0,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [1,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0,1,0,0]
]

RAW_BOARD_2 = [
    [1,0,0,0,1,0,0,0,0,0,0,2,0],
    [0,0,0,0,0,2,0,0,0,0,0,7,2],
    [0,0,5,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,5,0,0,0,2,0,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,2,0,0,0,2,0,0,5,0,0,0],
    [0,2,0,0,0,1,1,2,0,0,0,0,2]
]

RAW_BOARD_3 = [
    [4,3,0,0,0,4,0,0,0,0,0,0,4],
    [0,3,0,4,0,0,0,0,0,4,3,0,0],
    [0,0,0,0,0,0,0,0,4,3,0,0,0],
    [0,0,0,0,0,3,0,4,3,0,0,0,0],
    [8,0,0,0,0,0,0,0,0,0,0,0,3],
    [0,0,0,0,0,0,0,3,4,0,0,0,0],
    [0,0,3,0,0,0,0,0,3,3,0,0,0],
    [0,4,0,0,0,4,0,0,0,3,4,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,3]
]

RAW_BOARD_4 = [
    [0,3,0,0,0,0,3,0,0,0,0,0,0],
    [2,0,0,2,0,4,0,0,0,3,0,0,0],
    [0,0,0,0,0,0,0,0,3,0,0,4,0],
    [0,0,0,0,0,3,0,0,0,0,0,0,0],
    [8,2,0,0,0,0,4,0,0,4,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,4,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,4,0,3,0,0,3,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,3,0,0,0,4]
]

RAW_BOARD_5 = [
    [1,0,0,0,0,4,0,0,0,0,4,0,0],
    [0,5,0,0,0,0,3,0,0,3,0,0,0],
    [8,0,0,2,0,0,0,0,0,6,0,0,3],
    [0,0,2,0,5,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,2,3,0,0,0,0,0],
    [0,0,0,0,0,0,0,6,0,0,0,0,0],
    [1,0,0,0,3,0,0,0,0,0,0,0,0],
    [0,5,0,2,0,0,4,0,0,0,6,0,0],
    [0,0,0,0,0,0,0,4,6,0,0,0,0]
]

MINIGAMES_DATA = {
    "1": {
        "player_pos": (0,5),
        "enemies": {
            "1": {
                "pos": (10,6),
                "alert": 3
            }
        },
        "goal": (12,2),
        "raw_board": RAW_BOARD_1
    },
    "2": {
        "player_pos": (2,2),
        "enemies": {
            "1": {
                "pos": (3,7),
                "alert": 3
            },
            "2": {
                "pos": (9,1),
                "alert": 3
            }
        },
        "goal": (11,1),
        "raw_board": RAW_BOARD_2
    },
    "3": {
        "player_pos": (11,4),
        "enemies": {
            "1": {
                "pos": (5,5),
                "alert": 20
            }
        },
        "goal": (0,4), # ASquí va libro
        "raw_board": RAW_BOARD_3
    },
    "4": {
        "player_pos": (12,1),
        "enemies": {
            "1": {
                "pos": (12,8),
                "alert": 20
            }
        },
        "goal": (0,4), # ASquí va libro
        "raw_board": RAW_BOARD_4
    },
    "5": {
        "player_pos": (12,7),
        "enemies": {
            "1": {
                "pos": (12,3),
                "alert": 20
            }
        },
        "goal": (0,2), # ASquí va libro
        "raw_board": RAW_BOARD_5
    }
}
# Locations buttons



# Level config
SHELTER_EXPIRATION_TIME = 2 + 1
# HUB
