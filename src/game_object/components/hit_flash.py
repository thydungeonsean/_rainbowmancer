from src.enum.hues import *
from src.enum.colors import *


class HitFlash(object):

    seq = (0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0)

    def __init__(self, color_component):
        self.color_component = color_component
        self.tick = 0

        self.flash_color = self.set_flash_color()
        self.base_color = self.set_base_color()

    @property
    def color_map(self):
        return self.color_component.color_map

    @property
    def pos(self):
        return self.color_component.owner.coord.int_position

    def run(self):

        self.tick += 1
        if self.tick >= len(HitFlash.seq):
            self.end_flash()

    def get_color(self):

        if HitFlash.seq[self.tick] == 1:
            return self.flash_color
        else:
            return self.base_color

    def set_flash_color(self):

        if self.color_component.is_generated:
            if self.color_component.hue_id in red_hits:
                return hue_table[RED_HUE][max_str]  # red flash
            else:
                return hue_table[WHITE_HUE][max_str]  # white flash
        else:
            if self.color_map.get_tile(self.pos) in red_hits:
                return hue_table[RED_HUE][max_str]  # red flash
            else:
                return hue_table[WHITE_HUE][max_str]

    def set_base_color(self):
        return self.color_component.get_current_base_color()

    def end_flash(self):
        self.color_component.hit_flashes.remove(self)
