from sub_map import SubMap
from src.enum.terrain import *


class TerrainMap(SubMap):

    def __init__(self, w, h, map_seed, level_map):

        SubMap.__init__(self, w, h, level_map)
        self.map_seed = map_seed

        self.secret = set()
        self.main_zone = set()
        self.exit_stair = None
        self.entrance = None

    @staticmethod
    def start_value():
        return WALL_

    def get_all(self, key):

        return filter(lambda x: self.get_tile(x) == key, self.all_points)

    def set_exit(self, point):
        self.set_tile(point, EXIT_DOOR_)
        self.exit_stair = point

    def set_entrance(self, point):
        self.entrance = point

    def point_is_blocked(self, (x, y)):

        return self.get_tile((x, y)) in blocking_terrains

    def point_is_floor(self, point):
        return self.get_tile(point) == FLOOR_

    def point_is_shatterable(self, point):
        return not self.on_edge(point) and self.get_tile(point) in {STALAGTITE_, STONE_WALL_, WALL_}

    def on_edge(self, (x, y)):
        return x == 0 or x == self.w-1 or y == 0 or y == self.h-1

    def point_is_bindable(self, point):
        return self.get_tile(point) in {STALAGTITE_, STONE_WALL_, WALL_}
