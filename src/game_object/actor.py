from game_object import GameObject
from components.image_component import ImageComponent
from components.stat_component import StatComponent
from components.color_component import *


class Actor(GameObject):

    def __init__(self, level_map, coord, actor_id):

        GameObject.__init__(self, level_map, coord, False, True)
        self.stat_component = StatComponent(self, actor_id)
        self.image_component = ImageComponent(self, self.stat_component.image_id)
        self.color_component = self.initialize_color_component()
        self.position(self.coord.position)

    def initialize_color_component(self):
        hue_code = self.stat_component.stats['color_component']
        if hue_code > 0:  # is generator, not reflector
            color_component = ColorComponent(self, hue_id=hue_code, mode=GENERATE)
        else:
            color_component = ColorComponent(self, mode=REFLECT)

        return color_component

    def try_move(self, vector):

        if self.can_move(vector):
            self.move(vector)
        else:
            self.bump(vector)

    def can_move(self, vector):

        move_point = self.coord.peek_add(vector)

        terrain_block = self.level_map.terrain_map.point_is_blocked(move_point)
        object_block = self.level_map.object_manager.point_is_blocked(move_point)

        return not terrain_block and not object_block

    def move(self, vector):
        self.coord.add(vector)
        self.position(self.coord.position)
        self.on_move()
        # TODO update turn component

    def on_move(self):
        pass

    def bump(self, vector):

        target_coord = self.coord.peek_add(vector)
        bumped_target = self.level_map.object_manager.get_objects_at_point(target_coord)
        map(lambda x: x.on_bump(), bumped_target)

        used_turn = True
        if used_turn:
            # TODO update turn component
            pass
        pass

