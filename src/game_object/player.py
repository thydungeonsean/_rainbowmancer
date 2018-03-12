from actor import Actor
from src.map.color_components.color_source import ColorSource
from src.enum.hues import *
from src.sound.sounds import *


class Player(Actor):

    def __init__(self, level_map):
        Actor.__init__(self, level_map, (0, 0), 'rainbowmancer')
        # self.color_source = ColorSource(level_map, BLUE_HUE, 3, self.coord)

    def on_move(self):
        self.level_map.fov_map.recompute_fov()
        SoundArchive.get_instance().play_step()

    def reposition(self, (x, y)):  # for when player moves to to new depth of dungeon
        self.coord.set_position(x, y)
        self.set_position()
        # TODO if player has color source, add it to this map
