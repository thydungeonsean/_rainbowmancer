from element_component import ElementComponent
from src.image.icon_image import IconImage
from icon_color_component import IconColorComponent


class IconComponent(ElementComponent):

    def __init__(self, owner, icon_id, hue_id):

        ElementComponent.__init__(self, owner)

        self.image = self.set_icon_image(icon_id)
        self.image.position(self.owner.screen_coord)
        self.color_component = IconColorComponent(self, hue_id)

    def run(self):
        self.color_component.run()

    def draw(self, surface):

        self.image.draw(surface)

    def set_icon_image(self, icon_id):

        return IconImage(icon_id)

    def toggle_glow(self):

        if self.color_component.glowing:
            self.color_component.toggle_glow_off()
        else:
            self.color_component.toggle_glow_on()

    def toggle_active(self):

        if self.color_component.inactive:
            self.color_component.activate()
        else:
            self.color_component.deactivate()

    def deactivate(self):
        self.color_component.deactivate()

    def activate(self):
        self.color_component.activate()

    def start_glowing(self):
        self.color_component.toggle_glow_on()

    def stop_glowing(self):
        self.color_component.toggle_glow_off()

    def change_color(self, hue_id):
        self.color_component.change_hue(hue_id)

    def focus_on(self):
        self.color_component.focus_on()

    def focus_off(self):
        self.color_component.focus_off()

    @property
    def active(self):
        return not self.color_component.inactive
