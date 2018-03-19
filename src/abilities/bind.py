from ability import Ability
from src.enum.hues import *
from src.game_object.spell_objects.bound_terrain import BoundTerrain


class Bind(Ability):

    bindable_obj_ids = {
        'player', 'ally', 'summoned_wall', 'enemy', 'crystal', 'door', 'brazier', 'bound_terrain'
    }

    def __init__(self, manager):

        Ability.__init__(self, manager)

    @property
    def bind_hues(self):
        return Bind.bind_table[self.ability_hue]

    def can_be_cast(self):
        return self.panel.ability_color != WHITE_HUE

    def compute_valid_points(self):

        points = set()
        points.update(self.get_visible())
        points = set(filter(self.point_has_bind_target, points))

        self.valid_points.update(points)

    def point_has_bind_target(self, point):

        objects = self.object_manager.get_objects_at_point(point)
        if objects:
            return self.bindable_objects(objects)
        else:
            return self.bindable_terrain(point)

    def bindable_objects(self, objects):

        for obj in objects:

            if self.object_is_bindable(obj):
                return True

        return False

    def object_is_bindable(self, obj):

        return self.object_is_bindable_class(obj)

    def object_is_bindable_class(self, obj):

        return obj.obj_id in Bind.bindable_obj_ids

    def bindable_terrain(self, coord):

        return self.state.level.terrain_map.point_is_bindable(coord)

    def cast_ability(self, coord):

        # TODO play bind sound

        objects = self.object_manager.get_objects_at_point(coord)
        if objects:
            map(self.bind_object, objects)
        if self.bindable_terrain(coord):
            self.bind_terrain(coord)

        self.player.spend_turn()

    def bind_terrain(self, coord):

        binding = BoundTerrain(self.state.level, coord, self.ability_hue)
        self.object_manager.add_object(binding)

    def bind_object(self, obj):
        obj.bind(self.ability_hue)
