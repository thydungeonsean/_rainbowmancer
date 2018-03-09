from src.map._map import _Map
from src.enum.hues import *


class HueMap(_Map):

    def __init__(self, color_map, hue):

        self.color_map = color_map
        _Map.__init__(self, color_map.w, color_map.h)

        self.prev_map = [x[:] for x in self.map]
        self.hue = hue

    def compute(self):

        self.copy_map()
        map(self.reset_tile, self.all_points)

        for source in self.color_map.sources:

            if self.hue in hue_contains[source.hue]:
                self.set_tile(source.coord.int_position, source.strength)

        self.spread_color()

    def copy_map(self):

        def copy_tile(self, (x, y)):
            self.prev_map[x][y] = self.get_tile((x, y))

        map(lambda coord: copy_tile(self, coord), self.all_points)

    def reset_tile(self, (x, y)):
        self.set_tile((x, y), 0)

    def spread_color(self):

        max_strength = 5
        for s in range(max_strength, 0, -1):

            points_at_str = filter(lambda crd: self.get_tile(crd) == s, self.all_points)

            adj = self.get_adj_points(points_at_str)

            for point in adj:
                if self.get_tile(point) < s-1:
                    self.set_tile(point, s-1)

    def get_adj_points(self, points):
        edge = set()
        for point in points:
            adj = set(self.get_adj(point))
            edge.update(adj)
        return list(edge)

    def get_differing_tiles(self):

        diff = set()
        for x, y in self.all_points:
            if self.prev_map[x][y] != self.get_tile((x, y)):
                diff.add((x, y))

        return diff
