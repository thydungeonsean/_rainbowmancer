from state_component import StateComponent
from src.data_structures.vector import Vector


class View(StateComponent):

    VIEW_W = 27
    VIEW_H = 15

    OFFSET_X = VIEW_W / 2
    OFFSET_Y = VIEW_H / 2

    def __init__(self, state, map_w, map_h, start_pos=Vector(0, 0)):

        StateComponent.__init__(self, state)
        self.coord = start_pos
        self.display_w = View.VIEW_W
        self.display_h = View.VIEW_H

        self.min_x = 0
        self.min_y = 0
        self.max_x = map_w - self.display_w
        self.max_y = map_h - self.display_h

        self.offset_vector = Vector(-View.OFFSET_X, -View.OFFSET_Y)

    def set_new_map(self, map_w, map_h):
        self.max_x = map_w - self.display_w
        self.max_y = map_h - self.display_h

        self.initialize()

    def initialize(self):

        self.set_view_position()

    def get_offset_vector(self):

        self.offset_vector.set_position(-View.OFFSET_X, -View.OFFSET_Y)
        self.offset_vector.add(self.state.player.coord)

    def set_view_position(self):

        self.get_offset_vector()
        self.coord.set_position(self.offset_vector.x, self.offset_vector.y)
        self.limit_coord()

    def limit_coord(self):

        x, y = self.coord.position

        if x < self.min_x:
            x = self.min_x
        elif x > self.max_x:
            x = self.max_x

        if y < self.min_y:
            y = self.min_y
        elif y > self.max_y:
            y = self.max_y

        self.coord.set_position(x, y)

    def coord_in_view(self, pos):
        x, y = pos.position
        vx, vy = self.coord.position
        return vx <= x < vx + self.display_w and vy <= y < vy + self.display_h
