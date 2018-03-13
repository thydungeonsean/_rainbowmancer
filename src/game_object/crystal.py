from game_object import GameObject
from components.color_component import *
from components.image_component import ImageComponent
from src.map.color_components.color_source import ColorSource
from src.enum.objects import CRYSTAL
from src.sound.sounds import *


class Crystal(GameObject):

    def __init__(self, level_map, coord, hue_id):

        GameObject.__init__(self, level_map, coord, False, True)
        self.image_component = ImageComponent(self, CRYSTAL)
        self.color_component = self.create_color_component(hue_id)
        self.color_source = ColorSource(level_map, hue_id, 5, self.coord)

        self.health = 3

    @property
    def dead(self):
        return self.health <= 0

    def create_color_component(self, hue_id):

        return ColorComponent(self, hue_id, mode=GENERATE)

    def on_bump(self, bumper):

        if bumper.team == "PLAYER":
            self.take_hit()
            self.color_component.add_hit_flash()
            bumper.spend_turn()
        else:
            bumper.spend_turn()
            #raise Exception('why enemy try to bump crystal?')

    def take_hit(self):

        self.health -= 1
        if self.health > 0:
            SoundArchive.get_instance().play_sound('pick1')
        else:
            pass
            # TODO shatter sound
            SoundArchive.get_instance().play_sound('hit2')

        if self.health <= 0:
            self.shatter()

    def shatter(self):

        self.level_map.object_manager.request_update()
        self.color_source.kill()

        # TODO
        # change tile
        # boost player inventory

