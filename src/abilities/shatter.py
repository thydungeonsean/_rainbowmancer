from ability import Ability
from src.enum.hues import *


class Shatter(Ability):

    shatter_table = {
        RED_HUE: {GREEN_HUE},
        GREEN_HUE: {BLUE_HUE},
        BLUE_HUE: {RED_HUE},
        YELLOW_HUE: {PURPLE_HUE, BLUE_HUE},
        CYAN_HUE: {YELLOW_HUE, RED_HUE},
        PURPLE_HUE: {CYAN_HUE, GREEN_HUE}
    }

    shatterable_obj_ids = {
        'player', 'ally', 'summoned_wall', 'enemy', 'crystal', 'door', 'brazier', 'bound_terrain'
    }

    def __init__(self, manager):

        Ability.__init__(self, manager)

    @property
    def shatter_hues(self):

        return Shatter.shatter_table[self.ability_hue]

    def can_be_cast(self):
        
        return self.panel.ability_color != WHITE_HUE

    def compute_valid_points(self):

        points = set()
        points.update(self.get_visible())
        points = set(filter(self.point_is_shatterable, points))

        self.valid_points.update(points)

    def point_is_shatterable(self, point):

        objects = self.object_manager.get_objects_at_point(point)
        if objects:
            return self.shatterable_objects(objects)
        else:
            return self.shatterable_color(point) and self.shatterable_terrain(point)

    def shatterable_objects(self, objects):

        for obj in objects:

            if self.object_is_shatterable(obj):
                return True

        return False

    def object_is_shatterable(self, obj):

        return self.object_is_shatterable_class(obj) and obj.color_component.current_hue in self.shatter_hues

    def object_is_shatterable_class(self, obj):

        return obj.obj_id in Shatter.shatterable_obj_ids

    def shatterable_color(self, coord):

        return self.color_map.get_tile(coord) in self.shatter_hues

    def shatterable_terrain(self, coord):

        return self.state.level.terrain_map.point_is_shatterable(coord)

    def cast_ability(self, coord):

        # TODO play shatter sound

        objects = self.object_manager.get_objects_at_point(coord)
        if objects:
            map(self.shatter_object, objects)
        if self.shatterable_terrain(coord):
            self.shatter_terrain(coord)

        self.player.spend_turn()

    def shatter_object(self, obj):

        obj.shatter()

    def shatter_terrain(self, coord):

        self.state.level.shatter_terrain(coord)
