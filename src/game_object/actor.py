from game_object import GameObject
from components.image_component import ImageComponent
from components.stat_component import StatComponent
from components.color_component import *
from components.turn_component import TurnComponent


class Actor(GameObject):

    def __init__(self, level_map, coord, actor_id):

        GameObject.__init__(self, level_map, coord, False, True)
        self.stat_component = StatComponent(self, actor_id)
        self.image_component = ImageComponent(self, self.stat_component.image_id)
        self.color_component = self.initialize_color_component()
        self.turn_component = TurnComponent(self)
        self.position(self.coord.position)

        self.team = self.set_team()

    def set_team(self):
        return 'AI'

    def initialize_color_component(self):
        hue_code = self.stat_component.stats['color_component']
        if hue_code > 0:  # is generator, not reflector
            color_component = ColorComponent(self, hue_id=hue_code, mode=GENERATE)
        else:
            color_component = ColorComponent(self, mode=REFLECT)

        return color_component

    @property
    def dead(self):
        return self.stat_component.dead

    def try_move(self, vector):

        if self.can_move(vector):
            self.move(vector)
            self.spend_turn()
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
        map(lambda x: x.on_bump(self), bumped_target)

        used_turn = True
        if used_turn:
            # TODO update turn component
            pass
        pass

    def spend_turn(self):
        self.turn_component.take_turn()

    def refresh(self):
        self.turn_component.refresh_turn()

    def attack(self, foe):

        self.stat_component.attack(foe)
        self.spend_turn()

    @property
    def ready(self):
        return self.turn_component.ready


