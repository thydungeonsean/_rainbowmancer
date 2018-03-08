from cave_map_generator import CaveMapGen
from src.map.level_map import LevelMap
from src.map.tile_map import TileMap
from src.map.color_map import ColorMap
from src.map.fov_map import FOVMap
from src.image.map_image import MapImage

from random import seed, choice, sample

from src.enum.hues import *


class LevelGen(object):

    map_seed = None

    @classmethod
    def generate_level(cls, game_state, map_seed):
        # TODO - take in a depth argument etc and use a template for that depth to choose monsters, items, etc.

        level = LevelMap(game_state, map_seed)
        cls.map_seed = level.map_seed

        terrain_map = CaveMapGen.generate_cave_terrain_map(45, 25, cls.map_seed, level)

        cls.initialize_level(level, terrain_map)

        # cls.initialize_color_sources(level)
        # cls.create_door_objects(level)
        #
        cls.initialize_fov(level)

        # cls.spawn_monsters(level, 12)

        level.map_image = MapImage(level)

        return level

    @classmethod
    def initialize_level(cls, level, terrain_map):

        level.terrain_map = terrain_map

        level.tile_map = TileMap(level)
        level.tile_map.initialize()

        level.color_map = ColorMap(level)

        level.color_map.add_color_source(RED_HUE, 5, (10, 10))
        level.color_map.compute_color_map()
        # level.color_source_generator.set_color_map(level.color_map)

    @classmethod
    def initialize_color_sources(cls, level):

        seed(cls.map_seed)

        crystals = filter(lambda x: level.terrain_map.get_tile_id(x) == 'large_crystal', level.terrain_map.all_points)

        for point in crystals:
            color = choice(('red', 'green', 'blue'))
            level.map_object_generator.add_crystal(point, color)
            #level.color_source_generator.get_color_source(point, color, 5)

        level.color_map.recompute_maps()

        braziers = filter(lambda x: level.terrain_map.get_tile_id(x) == 'brazier', level.terrain_map.all_points)

        for point in braziers:
            level.map_object_generator.add_brazier(point)

    @classmethod
    def create_door_objects(cls, level):

        doors = filter(lambda x: level.terrain_map.get_tile_id(x) == 'door', level.terrain_map.all_points)

        for point in doors:
            level.map_object_generator.add_door(point)

    @classmethod
    def initialize_fov(cls, level):

        level.fov_map = FOVMap(level)
        level.fov_map.init_fov_map()

    @classmethod
    def spawn_monsters(cls, level, num):

        seed(cls.map_seed)

        level.fov_map.recompute_fov(center=level.terrain_map.entrance)
        visible = level.fov_map.get_visible_points(level.terrain_map.entrance)

        floor = set(filter(lambda x: level.terrain_map.get_tile(x) == 0, level.terrain_map.all_points))

        spawn_locations = floor.difference(visible)  # all floor locations not in fov for player start

        # TODO added weigthed algorithm to space monsters better later
        monster_points = sample(spawn_locations, num)

        for point in monster_points:
            level.map_object_generator.add_random_monster(point)

