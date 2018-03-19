from ..game_object import GameObject
from src.map.color_components.color_source import ColorSource
from duration_component import DurationComponent


class SummonedColor(GameObject):

    summon_str = 4

    def __init__(self, level_map, coord, hue_id):

        GameObject.__init__(self, level_map, coord, False, False)

        self.duration_component = DurationComponent(self, SummonedColor.summon_str)
        self.color_source = ColorSource(self.level_map.color_map, hue_id, SummonedColor.summon_str, self.coord)

    @property
    def dead(self):
        return self.duration_component.is_complete()

    def spend_turn(self):
        self.duration_component.tick()
        if self.duration_component.over():
            self.end()
        else:
            self.update_color_source()

    def update_color_source(self):
        self.color_source.change_strength(self.duration_component.duration)

    def end(self):
        self.color_source.kill()
        self.duration_component.end()
