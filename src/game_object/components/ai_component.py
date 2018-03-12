from game_object_component import GameObjectComponent
from random import *
from src.data_structures.vector import Vector


class AIComponent(GameObjectComponent):

    def __init__(self, owner):

        GameObjectComponent.__init__(self, owner)

    @property
    def level(self):
        return self.owner.level_map

    def take_turn(self):
        self.random_walk()

    def random_walk(self):

        adj = self.get_adj()
        if adj:

            x, y = choice(adj)
            vec = Vector(x, y)
            vec.sub(self.owner.coord)
            self.owner.try_move(vec)

        else:
            self.owner.spend_turn()

    def get_adj(self):

        return filter(lambda x: not self.point_is_blocked(x), self.level.terrain_map.get_adj(self.owner.coord.int_position))

    def point_is_blocked(self, point):
        return self.level.terrain_map.point_is_blocked(point)

