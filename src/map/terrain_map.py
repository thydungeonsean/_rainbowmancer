from sub_map import SubMap
from src.enum.terrain import *


class TerrainMap(SubMap):

    def __init__(self, w, h, map_seed, level_map=None):

        SubMap.__init__(self, w, h, level_map)
        self.map_seed = map_seed

        self.secret = {}
        self.main_zone = {}
        self.exit = None
        self.entrance = None

    def start_value():
        return WALL_

    def get_all(self, key):

        return filter(lambda x: self.get_tile(x) == key, self.all_points)

    def set_exit(self, point):
        self.set_tile(point, EXIT_DOOR_)
        self.exit = point

    def set_entrance(self, point):
        self.entrance = point
