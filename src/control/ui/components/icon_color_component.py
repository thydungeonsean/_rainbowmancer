import src.enum.hues as hues
from icon_glow_component import IconGlowComponent
from src.enum.hues import *

WHITE_HUE = hues.WHITE_HUE


class IconColorComponent(object):

    def __init__(self, owner, hue_id):

        self.owner = owner

        self.hue_id = hue_id
        self.color_id = None
        self.glow_component = IconGlowComponent(self.owner, self)

        self.glowing = False
        self.inactive = False
        self.focus = False
        self.needs_update = True

        self.update_color()

    @property
    def color_map(self):
        return self.owner.level_map.color_map

    def run(self):

        self.glow_component.run()

        if self.needs_update:
            self.update_color()
            self.needs_update = False

    def get_color(self):
        return self.color_id

    def request_update(self):
        self.needs_update = True

    def update_color(self):

        self.color_id = self.update()
        self.owner.image.change_color(self.color_id)

    def update(self):

        if self.inactive:
            color_id = hue_table[self.hue_id][0]
        elif not self.focus:
            color_id = hue_table[self.hue_id][max_str]
        elif self.glowing:
            color_id = self.glow_component.get_boost_flash()
        else:
            color_id = hues.hue_table[self.hue_id][hues.max_str]

        return color_id

    def deactivate(self):

        self.inactive = True
        self.request_update()

    def activate(self):
        self.inactive = False
        self.request_update()

    def toggle_glow_on(self):
        self.glowing = True

    def toggle_glow_off(self):
        self.glowing = False

    def change_hue(self, new_hue):

        self.hue_id = new_hue
        self.request_update()

    def focus_on(self):
        self.focus = True

    def focus_off(self):
        self.focus = False
