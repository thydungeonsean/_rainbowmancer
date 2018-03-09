from sub_map import SubMap
from color_components.hue_map import HueMap
from src.enum.hues import *


class ColorMap(SubMap):
    
    def __init__(self, level_map):

        SubMap.__init__(self, level_map.w, level_map.h, level_map)

        self.hue_maps = {
            RED_HUE: HueMap(self, RED_HUE),
            GREEN_HUE: HueMap(self, GREEN_HUE),
            BLUE_HUE: HueMap(self, BLUE_HUE),
        }

        self.sources = []
        self.needs_recompute = True

    def get_tile_color(self, point):

        if self.fov_map.point_is_visible(point):

            hue = self.get_tile(point)
            if hue == DARK_HUE:
                strength = 1
            else:
                strength = self.get_strength(point)

            return hue_table[hue][strength]
        else:
            return hue_table[DARK_HUE][0]

    def get_strength(self, point):

        return max([hue_map.get_tile(point) for hue_map in self.hue_maps.itervalues()])

    def compute_color_map(self):

        for hue_map in self.hue_maps.itervalues():
            hue_map.compute()

        for x, y in self.all_points:

            red = self.hue_maps[RED_HUE].get_tile((x, y)) > 0
            green = self.hue_maps[GREEN_HUE].get_tile((x, y)) > 0
            blue = self.hue_maps[BLUE_HUE].get_tile((x, y)) > 0

            if red and green and blue:
                self.set_tile((x, y), WHITE_HUE)
            elif red and green:
                self.set_tile((x, y), YELLOW_HUE)
            elif red and blue:
                self.set_tile((x, y), PURPLE_HUE)
            elif green and blue:
                self.set_tile((x, y), CYAN_HUE)
            elif red:
                self.set_tile((x, y), RED_HUE)
            elif green:
                self.set_tile((x, y), GREEN_HUE)
            elif blue:
                self.set_tile((x, y), BLUE_HUE)
            else:
                self.set_tile((x, y), DARK_HUE)

        self.needs_recompute = False

    # color source managing
    def add_color_source(self, src):

        src.color_map = self
        self.sources.append(src)

        self.request_recompute()

    def request_recompute(self):
        self.needs_recompute = True

    def get_differing_tiles(self):

        diff = set()

        for hue_map in self.hue_maps.itervalues():
            diff.update(hue_map.get_differing_tiles())

        return diff
