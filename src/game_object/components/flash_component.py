from game_object_component import GameObjectComponent
from src.enum.colors import *
from src.enum.hues import *


class FlashComponent(GameObjectComponent):

    CYCLE = 24
    HALF_CYCLE = CYCLE / 2

    def __init__(self, owner, color):

        GameObjectComponent.__init__(self, owner)
        self.color_component = color

        self.pol = 1
        self.tick = 0

    def run(self):

        self.tick += 1

        if self.tick >= FlashComponent.CYCLE:
            self.tick = 0
            self.pol = 1
        elif self.tick == FlashComponent.HALF_CYCLE:
            self.pol = -1

        if self.is_boosted or self.is_vulnerable or self.owner.critical:
            self.color_component.request_update()

    @property
    def color_map(self):
        return self.owner.level_map.color_map

    @property
    def is_boosted(self):
        return self.matches_tile_color()

    @property
    def is_vulnerable(self):
        return self.is_opposed_to_tile_color()

    @property
    def pos(self):
        return self.owner.coord.int_position

    def matches_tile_color(self):

        if self.color_component.hue_id != WHITE_HUE:
            return self.color_map.get_tile(self.pos) == self.color_component.hue_id
        else:
            return False

    def is_opposed_to_tile_color(self):

        tile_hue = self.color_map.get_tile(self.pos)
        object_hue = self.color_component.hue_id

        return tile_hue in opposed_hues[object_hue]

    def get_critical_flash(self):
        if self.color_component.is_generated:
            bot = LT_BLACK
            top = hue_table[self.color_component.hue_id][max_str]
        elif self.color_map.get_tile(self.pos) not in {WHITE_HUE, DARK_HUE}:
            bot = LT_BLACK
            top = hue_table[self.color_map.get_tile(self.pos)][max_str]
        else:
            bot = PURE_BLACK
            top = RED_2
        return self.interpolate_colors(bot, top, self.get_progress_percentage())

    def get_boost_flash(self):
        bot = hue_table[self.color_component.hue_id][max_str]
        top = WHITE
        return self.interpolate_colors(bot, top, self.get_progress_percentage())

    def get_progress_percentage(self):

        if self.pol == 1:
            return float(self.tick) / FlashComponent.HALF_CYCLE
        else:
            diff = self.tick - FlashComponent.HALF_CYCLE
            mod = FlashComponent.HALF_CYCLE - diff
            return float(mod) / FlashComponent.HALF_CYCLE

    def interpolate_colors(self, (br, bg, bb), (tr, tg, tb), percent):

        diff_r = int((tr - br) * percent)
        diff_g = int((tg - bg) * percent)
        diff_b = int((tb - bb) * percent)

        return diff_r + br, diff_g + bg, diff_b + bb
