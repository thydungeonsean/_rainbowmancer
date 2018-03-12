from src.data_structures.vector import Vector
from src.config import *


class GameObject(object):

    def __init__(self, level_map, (x, y), blocks_sight, blocks):

        self.level_map = level_map
        self.game_state = level_map.game_state
        self.view = self.game_state.view

        self.coord = Vector(x, y)

        self.image_component = None
        self.color_component = None
        self.stat_component = None
        self.color_source = None

        self.team = 'NEUTRAL'

        self.blocks_sight = blocks_sight
        self.blocks = blocks

    @property
    def dead(self):
        return False

    def refresh(self):
        pass

    def run(self):

        if self.color_component:
            self.color_component.run()

    def draw(self, surface):
        if self.image_component:
            self.image_component.draw(surface)

    def set_position(self):

        self.position(self.coord.position)

    def position(self, (x, y)):

        x, y = self.get_relative_coord((x, y))

        if self.image_component:
            self.image_component.position((x * SCALE_TILE_W, y * SCALE_TILE_H))
        if self.color_component:
            self.color_component.request_update()
        if self.color_source:
            self.color_source.move()

    def get_relative_coord(self, (x, y)):
        vx, vy = self.view.coord.position
        return x - vx, y - vy

    def on_bump(self, bumper):
        # called when an actor bumps this game object
        pass

    def request_update(self):

        if self.color_component:
            self.color_component.request_update()
