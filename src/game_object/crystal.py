from game_object import GameObject
from components.color_component import *


class Crystal(GameObject):

    def __init__(self, level_map, coord, hue_id):

        GameObject.__init__(self, level_map, coord, False, True)
        self.color_component = self.create_color_component(hue_id)
        # TODO add color source to color map as well

    def create_color_component(self, hue_id):

        return ColorComponent(self, hue_id, mode=GENERATE)

    def on_bump(self):

        print 'bump crystal'
