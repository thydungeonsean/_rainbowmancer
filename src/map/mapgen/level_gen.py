from cave_map_generator import CaveMapGen
from src.map.level_map import LevelMap
from src.map.tile_map import TileMap
from src.map.color_map import ColorMap
from src.map.fov_map import FOVMap
from src.image.map_image import MapImage

from random import seed, choice, sample

from src.enum.terrain import *
from src.enum.hues import *

from src.game_object.door import Door
from src.game_object.crystal import Crystal
from src.game_object.brazier import Brazier
from src.game_object.exit import Exit

from monster_generator import MonsterGenerator


class LevelGen(object):

    # min width, 30 for map scrolling

    map_seed = None

    @classmethod
    def generate_level(cls, game_state, depth, map_seed=None):

        width = 40
        height = 25

        level = LevelMap(game_state, depth, map_seed)
        cls.map_seed = level.map_seed

        number_of_crystals = 10
        number_of_monsters = 12

        terrain_map = CaveMapGen.generate_cave_terrain_map(width, height, number_of_crystals, map_seed, level)

        cls.initialize_level(level, terrain_map)
        cls.initialize_fov(level)

        # adding game objects to the level
        cls.create_doors(level)
        cls.create_crystals(level)
        cls.create_braziers(level)
        cls.create_exit(level)

        cls.initialize_color(level)

        cls.spawn_monsters(level, number_of_monsters)

        level.map_image = MapImage(level)

        return level

    @classmethod
    def initialize_fov(cls, level):

        level.fov_map = FOVMap(level)
        level.fov_map.init_fov_map()

    @classmethod
    def initialize_level(cls, level, terrain_map):

        level.terrain_map = terrain_map

        level.tile_map = TileMap(level)
        level.tile_map.initialize()

        level.color_map = ColorMap(level)

        level.color_map.compute_color_map()

    @classmethod
    def initialize_color(cls, level):
        level.color_map.compute_color_map()

    @classmethod
    def create_doors(cls, level):

        doors = level.terrain_map.get_all(DOOR_)

        for point in doors:

            door = Door(level, point)
            level.add_object(door)

    @classmethod
    def create_crystals(cls, level):

        crystals = level.terrain_map.get_all(CRYSTAL_)
        hues = [RED_HUE, GREEN_HUE, BLUE_HUE, CYAN_HUE, YELLOW_HUE, PURPLE_HUE, WHITE_HUE]

        for point in crystals:

            hue = choice(hues)

            crystal = Crystal(level, point, hue)
            level.add_object(crystal)

        cls.initialize_color(level)

    @classmethod
    def create_braziers(cls, level):

        braziers = level.terrain_map.get_all(BRAZIER_)

        for point in braziers:

            brazier = Brazier(level, point)
            level.add_object(brazier)

    @classmethod
    def create_exit(cls, level):

        exit_point = level.exit_stair

        exit_obj = Exit(level, exit_point, level.depth+1)
        level.add_object(exit_obj)

    @classmethod
    def spawn_monsters(cls, level, num):

        seed(cls.map_seed)

        level.fov_map.recompute_fov(center=level.terrain_map.entrance)
        visible = level.fov_map.get_visible_points(level.terrain_map.entrance)

        floor = set(level.terrain_map.get_all(FLOOR_))

        spawn_locations = floor.difference(visible)  # all floor locations not in fov for player start

        # TODO added weighted algorithm to space monsters better later
        monster_points = sample(spawn_locations, num)

        MonsterGenerator.get_instance().spawn_monsters(level, monster_points)

