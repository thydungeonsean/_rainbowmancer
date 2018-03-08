from src.enum.tiles import *
from src.enum.objects import *


tile_key = {

    # player
    RAINBOWMANCER: (0, 0),

    # tiles
    BRAZIER_LIT: (1, 0),
    BRAZIER_UNLIT: (2, 0),

    CRYSTAL: (9, 0),
    CRYSTAL_SMALL: (10, 0),

    STONE_WALL_VER: (1, 2),
    STONE_WALL_HOR_1: (2, 1),
    STONE_WALL_HOR_2: (3, 1),

    CAVE_WALL_VER: (1, 2),
    CAVE_WALL_HOR_1: (2, 2),
    CAVE_WALL_HOR_2: (3, 2),

    EXIT_DOOR: (4, 0),

    DOOR_CLOSE: (4, 1),
    DOOR_OPEN: (4, 2),

    FLOOR: (5, 0),

    BLANK: (3, 0),

    STONE_1: (6, 0),
    STONE_2: (7, 0),
    STONE_3: (8, 0),

    VEG_1: (5, 1),
    VEG_2: (6, 1),
    VEG_3: (7, 1),
    VEG_4: (8, 1),

    TUFT_1: (5, 2),
    TUFT_2: (6, 2),

    STALAG_1: (7, 2),
    STALAG_2: (8, 2),
    MUSHROOM: (9, 2),

    # foes
    GNOME: (0, 3),

}
