from src.data_structures.vector import Vector
from src.config import *


class GameObject(object):

    def __init__(self, level_map, (x, y)):

        self.level_map = level_map
        self.game_state = level_map.game_state
        self.view = self.game_state.view

        self.coord = Vector(x, y)

        self.image_component = None

    def run(self):
        pass

    def draw(self, surface):
        if self.image_component:
            self.image_component.draw(surface)

    def set_position(self):

        self.position(self.coord.position)

    def position(self, (x, y)):

        x, y = self.get_relative_coord((x, y))

        if self.image_component:
            self.image_component.position((x * SCALE_TILE_W, y * SCALE_TILE_H))

    def get_relative_coord(self, (x, y)):
        vx, vy = self.view.coord.position
        return x - vx, y - vy
