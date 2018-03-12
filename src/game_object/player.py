from actor import Actor
from src.map.color_components.color_source import ColorSource
from src.enum.hues import *
from src.sound.sounds import *


class Player(Actor):

    def __init__(self, level_map, player_id='test'):
        Actor.__init__(self, level_map, (0, 0), player_id)
        # self.color_source = ColorSource(level_map, BLUE_HUE, 3, self.coord)

    def set_team(self):
        return 'PLAYER'

    def on_move(self):
        self.level_map.fov_map.recompute_fov()
        SoundArchive.get_instance().play_step()

    def on_bump(self, bumper):

        if bumper.team == "AI":
            bumper.attack(self)
        else:
            bumper.spend_turn()

    def reposition(self, (x, y)):  # for when player moves to to new depth of dungeon
        self.coord.set_position(x, y)
        self.set_position()
        # TODO if player has color source, add it to this map
