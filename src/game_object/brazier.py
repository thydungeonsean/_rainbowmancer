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

        self.state = None

        self.determine_initial_state()

        # TODO check it's tile, if lit use the animated and add color_source etc.

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
            self.color_source = ColorSource(self.level_map, tile_hue, Brazier.STRENGTH, self.coord)


