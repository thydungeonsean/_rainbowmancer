from src.enum.tiles import *
from src.enum.objects import *


tile_key = {

    # player
    RAINBOWMANCER: (0, 0),
    CYAN_KNIGHT: (1, 14),
    GEBBETH: (0, 14),
    YELLOWMANCER: (4, 14),
    CRIMLOCK: (5, 14),
    DWARF: (7, 14),

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
    GNOME_ENCHANTER: (1, 3),
    GNOME_MAGI: (2, 3),
    GNOME_TRICKSTER: (3, 3),

    FLAME: (4, 3),
    ORB: (5, 3),
    OOZE: (6, 3),
    DJIN: (7, 3),
    FLAMING_UNDEAD: (8, 3),

    NAGA: (0, 5),
    NAGA_ARCHER: (1, 5),
    NAGA_MAGE: (2, 5),

    KOBOLD: (3, 5),
    KOBOLD_ARCHER: (4, 5),
    KOBOLD_CHIEF: (5, 5),

    CENTAUR: (0, 7),
    CENTAUR_ARCHER: (1, 7),
    CENTAUR_CHIEF: (2, 7),

    FAE: (3, 7),
    FAE_WARRIOR: (4, 7),
    FAE_ENCHANTER: (5, 7),

    SKELETON: (0, 9),
    SKELETON_ARCHER: (1, 9),
    LICH: (2, 9),

    DARK_ELF: (3, 9),
    SPIDER: (4, 9),
    DARK_WIZARD: (5, 9),

    # summons

    VINE_WALL: (7, 9),
    TREANT: (8, 9),

}
