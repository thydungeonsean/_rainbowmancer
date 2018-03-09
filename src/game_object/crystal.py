from game_object import GameObject
from components.color_component import *
from components.image_component import ImageComponent
from src.map.color_components.color_source import ColorSource
from src.enum.objects import CRYSTAL


class Crystal(GameObject):

    def __init__(self, level_map, coord, hue_id):

        GameObject.__init__(self, level_map, coord, False, True)
        self.image_component = ImageComponent(self, CRYSTAL)
        self.color_component = self.create_color_component(hue_id)
        self.color_source = ColorSource(level_map, hue_id, 5, self.coord)

    def create_color_component(self, hue_id):

        return ColorComponent(self, hue_id, mode=GENERATE)

    def on_bump(self):

        print 'bump crystal'
