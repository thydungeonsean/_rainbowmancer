from game_object import GameObject
from src.map.color_components.color_source import ColorSource
from components.color_component import ColorComponent, REFLECT
from components.image_component import ImageComponent
from src.enum.objects import *
from src.enum.hues import *


class Brazier(GameObject):

    LIT = 1
    UNLIT = 0

    STRENGTH = 3

    def __init__(self, level_map, coord):

        GameObject.__init__(self, level_map, coord, False, True)

        self.obj_id = 'brazier'
        self.determine_initial_state()
        self.is_dead = False

        # TODO check it's tile, if lit use the animated and add color_source etc.

    @property
    def dead(self):
        return self.is_dead

    def on_bump(self, bumper):

        print 'bump brazier'

    def determine_initial_state(self):

        tile_hue = self.level_map.color_map.get_tile(self.coord.int_position)
        if tile_hue == DARK_HUE:
            self.state = Brazier.UNLIT
            self.image_component = ImageComponent(self, BRAZIER_UNLIT, animated=False)
            self.color_component = ColorComponent(self, WHITE_HUE, mode=REFLECT)
        else:
            self.state = Brazier.LIT
            self.image_component = ImageComponent(self, BRAZIER_LIT)
            self.color_component = ColorComponent(self, tile_hue, mode=REFLECT)
            self.color_source = ColorSource(self.level_map.color_map, tile_hue, Brazier.STRENGTH, self.coord)

    def shatter(self):
        self.is_dead = True
        self.level_map.object_manager.request_update()

        self.level_map.shatter_terrain(self.coord.int_position)

        # if lit, kill the color source
        if self.state == Brazier.LIT:
            self.color_source.kill()
