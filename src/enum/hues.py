from colors import *


# hue codes
DARK_HUE = 0
RED_HUE = 255
GREEN_HUE = 254
BLUE_HUE = 253
YELLOW_HUE = 252
CYAN_HUE = 251
PURPLE_HUE = 250
WHITE_HUE = 249


# shade tables
dark_shades = {0: UNSEEN, 1: GREY_0}

red_shades = {0: RED_SUB, 1: RED_1, 2: RED_2, 3: RED_3, 4: RED_4, 5: RED_5}

green_shades = {0: GREEN_SUB,1: GREEN_1, 2: GREEN_2, 3: GREEN_3, 4: GREEN_4, 5: GREEN_5}

blue_shades = {0: BLUE_SUB, 1: BLUE_1, 2: BLUE_2, 3: BLUE_3, 4: BLUE_4, 5: BLUE_5}

yellow_shades = {0: YELLOW_SUB, 1: YELLOW_1, 2: YELLOW_2, 3: YELLOW_3, 4: YELLOW_4, 5: YELLOW_5}

cyan_shades = {0: CYAN_SUB, 1: CYAN_1, 2: CYAN_2, 3: CYAN_3, 4: CYAN_4, 5: CYAN_5}

purple_shades = {0: PURPLE_SUB, 1: PURPLE_1, 2: PURPLE_2, 3: PURPLE_3, 4: PURPLE_4, 5: PURPLE_5}

white_shades = {0: GREY_0, 1: GREY_1, 2: GREY_2, 3: GREY_3, 4: GREY_4, 5: GREY_5}


# hue range tables
hue_table = {
    DARK_HUE: dark_shades,
    RED_HUE: red_shades,
    GREEN_HUE: green_shades,
    BLUE_HUE: blue_shades,
    YELLOW_HUE: yellow_shades,
    CYAN_HUE: cyan_shades,
    PURPLE_HUE: purple_shades,
    WHITE_HUE: white_shades,
}

hue_contains = {
    WHITE_HUE: {RED_HUE, GREEN_HUE, BLUE_HUE},
    YELLOW_HUE: {RED_HUE, GREEN_HUE},
    PURPLE_HUE: {RED_HUE, BLUE_HUE},
    CYAN_HUE: {GREEN_HUE, BLUE_HUE},
    RED_HUE: {RED_HUE},
    GREEN_HUE: {GREEN_HUE},
    BLUE_HUE: {BLUE_HUE},
    DARK_HUE: set()
}

max_str = 5

opposed_hues = {
    RED_HUE: {BLUE_HUE, CYAN_HUE},
    GREEN_HUE: {RED_HUE, PURPLE_HUE},
    BLUE_HUE: {GREEN_HUE, YELLOW_HUE},
    YELLOW_HUE: {CYAN_HUE},
    CYAN_HUE: {PURPLE_HUE},
    PURPLE_HUE: {YELLOW_HUE},
    WHITE_HUE: set()
}

red_hits = {GREEN_HUE, BLUE_HUE, YELLOW_HUE, CYAN_HUE, WHITE_HUE, DARK_HUE}

strong_colors = {RED_HUE, BLUE_HUE, PURPLE_HUE}
