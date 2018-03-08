from game_object_component import GameObjectComponent
import src.enum.hues as hues


REFLECT = 0
GENERATE = 1
WHITE_HUE = hues.WHITE_HUE


class ColorComponent(GameObjectComponent):

    REFLECT = REFLECT
    GENERATE = GENERATE

    def __init__(self, owner, hue_id=WHITE_HUE, mode=REFLECT):

        GameObjectComponent.__init__(self, owner)

        self.mode = mode
        self.hue_id = hue_id
        self.color_id = None

        self.update_function = {
            ColorComponent.REFLECT: self.update_reflect,
            ColorComponent.GENERATE: self.update_generate
        }

        self.update_color()
        self.needs_update = True

    @property
    def color_map(self):
        return self.owner.level_map.color_map

    def run(self):
        if self.needs_update:
            self.update_color()
            self.needs_update = False
        # for flashing effects

    def get_color(self):
        return self.color_id

    def request_update(self):
        self.needs_update = True

    def update_color(self):
        self.update_function[self.mode]()
        self.owner.image_component.change_color(self.color_id)

    def update_reflect(self):
        self.color_id = self.color_map.get_tile_color(self.owner.coord.int_position)

    def update_generate(self):
        self.color_id = hues.hue_table[self.hue_id][hues.max_str]


