from ..game_object import GameObject
from duration_component import DurationComponent
from ..components.image_component import ImageComponent
from ..components.color_component import ColorComponent, GENERATE


class BoundTerrain(GameObject):

    duration = 16

    def __init__(self, level_map, coord, hue_id):

        GameObject.__init__(self, level_map, coord, False, False)

        self.obj_id = 'bound_terrain'
        self.image_component = ImageComponent(self, self.get_tile(coord), animated=False)
        self.color_component = ColorComponent(self, hue_id, mode=GENERATE)
        self.duration_component = DurationComponent(self, BoundTerrain.duration)

    def get_tile(self, coord):
        return self.level_map.tile_map.get_tile(coord)

    @property
    def dead(self):
        return self.duration_component.is_complete()

    def spend_turn(self):
        self.duration_component.tick()
        if self.duration_component.over():
            self.end()

    def end(self):
        self.duration_component.end()

    def on_bump(self, bumper):

        print 'bump bound terrain'

    def shatter(self):
        self.end()
        self.level_map.shatter_terrain(self.coord.int_position)
