from random import randint
from src.game_object.object_controllers.object_manager import ObjectManager
from color_components.redraw_manager import RedrawManager


class LevelMap(object):

    def __init__(self, game_state, depth, map_seed=None):

        self.game_state = game_state

        if map_seed is None:
            self.map_seed = randint(0, 999999)
        else:
            assert isinstance(map_seed, int)
            self.map_seed = map_seed

        self.depth = depth

        self.terrain_map = None
        self.tile_map = None
        self.color_map = None
        self.fov_map = None

        self.map_image = None
        self.redraw_manager = RedrawManager(self)

        self.player = None

        self.object_manager = ObjectManager(self)

    def initialize(self, player):

        self.add_player(player)
        self.player.position_on_level_map(self.entrance)
        self.fov_map.recompute_fov()
        self.map_image.create_map_image()

    @property
    def w(self):
        return self.terrain_map.w

    @property
    def h(self):
        return self.terrain_map.h

    @property
    def entrance(self):
        return self.terrain_map.entrance

    @property
    def exit_stair(self):
        return self.terrain_map.exit_stair

    def run(self):

        self.object_manager.run()
        self.redraw_manager.run()
        self.map_image.set_view_position()

    def draw(self, view_port):

        self.map_image.draw(view_port.surface)

        self.object_manager.draw(view_port.surface)

    def add_player(self, player):

        self.player = player
        self.player.level_map = self
        self.object_manager.add_object(player)

    def add_object(self, obj):
        self.object_manager.add_object(obj)

    def add_color_source(self, src):
        self.color_map.add_color_source(src)

    def update_object_positions(self):

        self.object_manager.update_positions()
