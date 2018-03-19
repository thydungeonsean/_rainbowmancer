from ability import Ability
from src.enum.hues import *
from src.game_object.spell_objects.summoned_wall import SummonedWall


class Block(Ability):

    def __init__(self, manager):

        Ability.__init__(self, manager)

    def compute_valid_points(self):

        points = set()
        points.update(self.get_visible())
        points = set(filter(self.point_is_clear, points))

        self.valid_points.update(points)

    def point_is_clear(self, point):

        if not self.point_is_floor(point):
            return False

        return self.no_objects_at_point(point)

    def point_is_floor(self, point):

        return self.state.level.terrain_map.point_is_floor(point)

    def no_objects_at_point(self, point):

        return not self.object_manager.point_is_blocked(point)

    def cast_ability(self, coord):

        # place block summon object depending on ability hue
        summon = SummonedWall(self.state.level, coord, self.ability_hue)
        self.object_manager.add_object(summon)
        self.player.spend_turn()
