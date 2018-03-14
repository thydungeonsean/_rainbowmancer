

BORDER_1_TL = 64
BORDER_1_TR = 65
BORDER_1_BL = 66
BORDER_1_BR = 67
BORDER_1_T = 68
BORDER_1_S = 69

BORDER_2_TL = 70
BORDER_2_TR = 71
BORDER_2_BL = 72
BORDER_2_BR = 73
BORDER_2_T = 74
BORDER_2_S = 75

HEART_FULL = 76
HEART_EMPTY = 77

UI_TILES = {BORDER_1_TL, BORDER_1_TR, BORDER_1_BR, BORDER_1_BL, BORDER_1_T, BORDER_1_S, BORDER_2_BL, BORDER_2_BR,
            BORDER_2_TL, BORDER_2_TR, BORDER_2_T, BORDER_2_S, HEART_EMPTY, HEART_FULL}

CRYSTAL_ICON = 78
BOLT = 79
BIND = 80
RAY = 81
SUMMON = 82
SHATTER = 83
BLOCK = 84
INVOKE = 85
IMBUE = 86

ability_id_to_string = {BOLT: 'bolt', BIND: 'bind', RAY: 'ray', SUMMON: 'summon', SHATTER: 'shatter',
                        BLOCK: 'block', INVOKE: 'invoke', IMBUE: 'imbue'}
ability_string_to_id = {v: k for (k, v) in ability_id_to_string.iteritems()}
