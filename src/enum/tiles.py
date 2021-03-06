
BLANK = -1

FLOOR = 0

CAVE_WALL_VER = 1
CAVE_WALL_HOR_1 = 2
CAVE_WALL_HOR_2 = 3

CAVE_WALL_HORS = [CAVE_WALL_HOR_1, CAVE_WALL_HOR_1, CAVE_WALL_HOR_2]

STONE_WALL_VER = 4
STONE_WALL_HOR_1 = 5
STONE_WALL_HOR_2 = 6

STONE_WALL_HORS = [STONE_WALL_HOR_1, STONE_WALL_HOR_1, STONE_WALL_HOR_2]

WALLS = [CAVE_WALL_HOR_1, CAVE_WALL_HOR_2, CAVE_WALL_VER, STONE_WALL_HOR_1, STONE_WALL_HOR_2, STONE_WALL_VER]

EXIT_DOOR = 7

DOOR_CLOSE = 8
DOOR_OPEN = 9

STONE_1 = 10
STONE_2 = 11
STONE_3 = 12

STONES = [STONE_1, STONE_2, STONE_3]

VEG_1 = 13
VEG_2 = 14
VEG_3 = 15
VEG_4 = 16

VEGS = [VEG_1, VEG_2, VEG_3, VEG_4]

TUFT_1 = 17
TUFT_2 = 18

TUFTS = [TUFT_1, TUFT_2]

MUSHROOM = 19

STALAG_1 = 20
STALAG_2 = 21

STALAGTITES = [STALAG_1, STALAG_2]

DECO_FLOOR = STONES + VEGS + TUFTS + [MUSHROOM]
