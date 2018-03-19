from game_object import GameObject
from src.enum.tiles import DOOR_OPEN
from src.sound.sounds import *
from components.color_component import ColorComponent
from components.image_component import ImageComponent
from src.enum.tiles import DOOR_CLOSE, DOOR_OPEN


class Door(GameObject):

    CLOSED = 0
    OPEN = 1

    tile = {CLOSED: DOOR_CLOSE, OPEN: DOOR_OPEN}

    def __init__(self, level_map, coord):

        GameObject.__init__(self, level_map, coord, True, True)

        self.state = Door.CLOSED
        self.obj_id = 'door'
        self.image_component = ImageComponent(self, self.load_tile_image(), animated=False)
        self.color_component = ColorComponent(self)
        self.is_dead = False

    @property
    def dead(self):
        return self.is_dead

    def load_tile_image(self):
        return Door.tile[self.state]

    def on_bump(self, bumper):

        if self.state == Door.CLOSED:
            self.open_door()
            bumper.spend_turn()

    def open_door(self, sound=True):

        self.state = Door.OPEN
        self.blocks = False
        self.blocks_sight = False
        self.level_map.fov_map.update_point(self.coord.int_position)
        self.image_component = ImageComponent(self, self.load_tile_image(), animated=False)

        if sound:
            SoundArchive.get_instance().play_door()

        # change tile of tile_map
        self.level_map.tile_map.update_tile(self.coord.int_position, DOOR_OPEN)
        self.level_map.fov_map.recompute_fov()

    def shatter(self):
        self.open_door(sound=False)
        self.level_map.shatter_terrain(self.coord.int_position)

        self.is_dead = True
        self.level_map.object_manager.request_update()
