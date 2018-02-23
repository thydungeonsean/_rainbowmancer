from actor import Actor
from src.enum.objects import RAINBOWMANCER


class Player(Actor):

    def __init__(self, level_map, coord):

        Actor.__init__(self, level_map, coord, RAINBOWMANCER)
        self.image_component.change_color((255, 100, 50))