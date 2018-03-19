from ..game_object import GameObject
from duration_component import DurationComponent
from ..components.image_component import ImageComponent
from ..components.color_component import ColorComponent, GENERATE
from src.enum.tiles import STONE_WALL_HOR_1


class SummonedWall(GameObject):

    duration = 16

    def __init__(self, level_map, coord, hue_id):

        GameObject.__init__(self, level_map, coord, True, True)

        self.obj_id = 'summoned_wall'
        self.image_component = ImageComponent(self, STONE_WALL_HOR_1, animated=False)
        self.color_component = ColorComponent(self, hue_id, mode=GENERATE)
        self.duration_component = DurationComponent(self, SummonedWall.duration)
        self.health = 5

    @property
    def dead(self):
        return self.duration_component.is_complete() or self.health <= 0

    def spend_turn(self):
        self.duration_component.tick()
        if self.duration_component.over():
            self.end()

    def end(self):
        self.duration_component.end()

    def on_bump(self, bumper):

        bumper.spend_turn()
        self.color_component.add_hit_flash()
        self.health -= 1
        if self.health <= 0:
            self.level_map.object_manager.request_update()
            # TODO crush sound
        else:
            # TODO hit sound
            pass

    def shatter(self):
        self.health = 0
        self.level_map.object_manager.request_update()
