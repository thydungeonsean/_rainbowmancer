from src.config import *
from src.state.components.view import View
from src.enum.hues import *
from src.enum.ui import *


border_frame_w = TILE_W * 2
border_frame_h = TILE_H * 2

side_panel_w = SCALE_SCREEN_W - View.view_w_px
side_panel_h = SCALE_SCREEN_H
side_panel_coord = (SCALE_SCREEN_W-side_panel_w, 0)

crystal_panel_w = 160 + border_frame_w
crystal_panel_h = ICON_H * 6 + border_frame_h
crystal_panel_coord = (0, 0)

ability_panel_w = side_panel_w
ability_panel_h = SCALE_SCREEN_H - crystal_panel_h
ability_panel_coord = (0, crystal_panel_h)

player_panel_w = side_panel_w - crystal_panel_w
player_panel_h = crystal_panel_h
player_panel_coord = (crystal_panel_w, 0)

crystal_sequence = (('red', RED_HUE), ('green', GREEN_HUE), ('blue', BLUE_HUE), ('yellow', YELLOW_HUE),
                    ('purple', PURPLE_HUE), ('cyan', CYAN_HUE))

ability_sequence = (('bolt', BOLT), ('bind', BIND), ('ray', RAY), ('summon', SUMMON), ('shatter', SHATTER),
                   ('block', BLOCK), ('invoke', INVOKE), ('imbue', IMBUE))
