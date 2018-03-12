from game_object import GameObject
from src.enum.tiles import DOOR_OPEN
from src.sound.sounds import *


class Door(GameObject):

    CLOSED = 0
    OPEN = 1

    def __init__(self, level_map, coord):

        GameObject.__init__(self, level_map, coord, True, True)

        self.state = Door.CLOSED

    def on_bump(self):

        if self.state == Door.CLOSED:
            self.open_door()

    def open_door(self):

        self.state = Door.OPEN
        self.blocks = False
        self.blocks_sight = False
        self.level_map.fov_map.update_point(self.coord.int_position)

        SoundArchive.get_instance().play_door()

        # TODO change tile of tile_map
        self.level_map.tile_map.update_tile(self.coord.int_position, DOOR_OPEN)
        self.level_map.fov_map.recompute_fov()
