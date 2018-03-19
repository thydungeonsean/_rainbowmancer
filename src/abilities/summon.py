from ability import Ability
from src.enum.hues import *
from src.game_object.spell_objects.summoned_color import SummonedColor


class Summon(Ability):

    def __init__(self, manager):

        Ability.__init__(self, manager)

    def can_be_cast(self):
        return self.panel.ability_color != WHITE_HUE

    def compute_valid_points(self):

        points = set()
        points.update(self.get_visible())
        points = set(filter(self.point_is_dark, points))

        self.valid_points.update(points)

    def point_is_dark(self, point):

        return self.color_map.get_tile(point) == DARK_HUE

    def cast_ability(self, coord):

        # create a color_source
        # add to color_map and request update
        summon = SummonedColor(self.state.level, coord, self.ability_hue)
        self.object_manager.add_object(summon)

        self.light_braziers(coord)
        self.player.spend_turn()
        # TODO play summon sound

    def light_braziers(self, coord):

        affected = self.get_affected_points(coord)
        for p in affected:
            if self.point_is_dark(p):
                self.light_inactive_brazier(p)

    def get_affected_points(self, coord):
        return []

    def light_inactive_brazier(self, point):
        # get obj at point from object_manager
        # if objects is brazier and unlit, light with ability hue
        pass
