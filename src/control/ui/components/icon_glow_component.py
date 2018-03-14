from src.game_object.components.glow_component import GlowComponent
from src.enum.colors import *
from src.enum.hues import *


class IconGlowComponent(GlowComponent):

    CYCLE = 50

    def __init__(self, owner, color_component):

        GlowComponent.__init__(self, owner, color_component)

    def run(self):

        self.tick += 1

        if self.tick >= GlowComponent.CYCLE:
            self.tick = 0
            self.pol = 1
        elif self.tick == GlowComponent.HALF_CYCLE:
            self.pol = -1

        if self.color_component.glowing and not self.color_component.inactive:
            self.color_component.request_update()
