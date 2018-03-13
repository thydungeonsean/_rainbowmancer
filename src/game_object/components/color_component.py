from game_object_component import GameObjectComponent
import src.enum.hues as hues
from src.enum.hues import *
from flash_component import FlashComponent
from hit_flash import HitFlash


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

        self.flash_component = FlashComponent(self.owner, self)
        self.hit_flashes = []

        self.update_function = {
            ColorComponent.REFLECT: self.update_reflect,
            ColorComponent.GENERATE: self.update_generate
        }

        self.update_color()
        self.needs_update = True

    @property
    def color_map(self):
        return self.owner.level_map.color_map

    @property
    def is_generated(self):
        return self.mode == ColorComponent.GENERATE

    def run(self):

        self.flash_component.run()

        if self.hit_flashes:
            self.run_hit_flashes()

        if self.needs_update:
            self.update_color()
            self.needs_update = False

    def run_hit_flashes(self):

        self.hit_flashes[0].run()
        self.request_update()

    def get_color(self):
        return self.color_id

    def request_update(self):
        self.needs_update = True

    def update_color(self):

        if self.hit_flashes:
            self.color_id = self.hit_flashes[0].get_color()
        elif self.owner.critical:
            self.color_id = self.flash_component.get_critical_flash()
        else:
            self.color_id = self.get_current_base_color()
        self.owner.image_component.change_color(self.color_id)

    def get_current_base_color(self):

        return self.update_function[self.mode]()

    def update_reflect(self):

        pos = self.owner.coord.int_position
        if self.color_map.get_tile(pos) == DARK_HUE:
            color_id = GREY_2
        elif self.color_map.get_tile(pos) == WHITE_HUE:
            color_id = GREY_5
        else:
            color_id = self.color_map.get_tile_color(pos)

        return color_id

    def update_generate(self):

        if self.flash_component.is_vulnerable:
            color_id = self.flash_component.get_critical_flash()
        elif self.flash_component.is_boosted:
            color_id = self.flash_component.get_boost_flash()
        else:
            color_id = hues.hue_table[self.hue_id][hues.max_str]

        return color_id

    def add_hit_flash(self):
        self.hit_flashes.append(HitFlash(self))
