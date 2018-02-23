from random import randint
from src.game_object.object_controllers.object_manager import ObjectManager


class LevelMap(object):

    def __init__(self, game_state, map_seed=None):

        self.game_state = game_state

        if map_seed is None:
            self.map_seed = randint(0, 999999)
        else:
            assert isinstance(map_seed, int)
            self.map_seed = map_seed

        self.terrain_map = None
        self.tile_map = None
        self.color_map = None
        self.fov_map = None

        self.map_image = None

        self.player = None

        self.object_manager = ObjectManager(self)

    @property
    def w(self):
        return self.terrain_map.w

    @property
    def h(self):
        return self.terrain_map.h

    @property
    def entrance(self):
        return self.terrain_map.entrance

    def draw(self, view_port):

        self.map_image.draw(view_port.surface)
        # draw visible game objects and effects
        self.object_manager.draw(view_port.surface)

    def add_player(self, player):

        self.player = player
        self.object_manager.add_object(player)

