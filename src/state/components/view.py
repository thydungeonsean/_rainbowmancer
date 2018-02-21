from state_component import StateComponent
from src.data_structures.vector import Vector


class View(StateComponent):

    def __init__(self, state, display_w, display_h, map_w, map_h, start_pos=Vector(0, 0)):

        StateComponent.__init__(self, state)
        self.coord = start_pos
        self.display_w = display_w
        self.display_h = display_h

        self.min_x = -map_w + self.display_w
        self.min_y = -map_h + self.display_h
        self.max_x = 0
        self.max_y = 0

    def move_view(self, vector):

        self.coord.add(vector)
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
