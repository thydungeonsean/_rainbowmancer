from sub_map import SubMap
from random import *
from src.enum.tiles import *
from src.enum.objects import *
from src.enum.terrain import *


class TileMap(SubMap):

    EMPTY_RATE = 65

    def __init__(self, level_map):

        assert level_map.terrain_map is not None

        w = level_map.w
        h = level_map.h
        self.map_seed = level_map.map_seed
        SubMap.__init__(self, w, h, level_map)

        self.tile_chooser = {
            FLOOR_: self.choose_floor_tile,
            WALL_: self.choose_cave_wall_tile,
            STONE_WALL_: self.choose_stone_wall_tile,
            DOOR_: self.set_door_tile,
            STALAGTITE_: self.choose_stalagtite_tile,
            CRYSTAL_: self.set_crystal_tile,
            BRAZIER_: self.set_brazier_tile,
            EXIT_DOOR_: self.set_exit_tile,
        }

    def point_is_animated(self, point):
        return self.get_tile(point) in ANIMATED_OBJECTS

    def initialize(self):
        # translate terrain_map tile data into specific tile keys
        seed(self.map_seed)
        for point in self.all_points:

            self.set_tile_id(point, self.terrain_map.get_tile(point))

    def set_tile_id(self, point, terrain):

        self.tile_chooser[terrain](point)

    def choose_floor_tile(self, point):
        if randint(0, 99) < TileMap.EMPTY_RATE:
            t = FLOOR
        else:
            t = choice(DECO_FLOOR)
        self.set_tile(point, t)

    def choose_wall_tile(self, (px, py), horizontal_tiles):

        below = (px, py + 1)
        if self.point_in_bounds(below) and self.terrain_map.get_tile(below) not in vertical_wall_markers:
            tile_code = choice(horizontal_tiles)
        else:
            tile_code = CAVE_WALL_VER

        self.set_tile((px, py), tile_code)

    def choose_cave_wall_tile(self, point ):
        self.choose_wall_tile(point, CAVE_WALL_HORS)

    def choose_stone_wall_tile(self, point):
        self.choose_wall_tile(point, STONE_WALL_HORS)

    def set_door_tile(self, point):
        self.set_tile(point, DOOR_CLOSE)

    def set_brazier_tile(self, point):
        self.set_tile(point, BRAZIER_UNLIT)

    def choose_stalagtite_tile(self, point):
        self.set_tile(point, choice(STALAGTITES))

    def set_crystal_tile(self, point):
        self.set_tile(point, CRYSTAL)

    def set_exit_tile(self, point):
        self.set_tile(point, EXIT_DOOR)
