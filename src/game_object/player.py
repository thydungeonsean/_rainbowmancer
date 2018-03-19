from actor import Actor
from src.map.color_components.color_source import ColorSource
from src.enum.hues import *
from src.sound.sounds import *


class Player(Actor):

    def __init__(self, level_map, player_id='test'):
        Actor.__init__(self, level_map, (0, 0), player_id)
        # self.color_source = ColorSource(level_map, BLUE_HUE, 3, self.coord)
        self.obj_id = 'player'

    def set_team(self):
        return 'PLAYER'

    def on_move(self):
        self.level_map.fov_map.recompute_fov()
        SoundArchive.get_instance().play_step()
        self.spend_turn(free=True)

    def on_bump(self, bumper):

        if bumper.team == "AI":
            bumper.attack(self)
        else:
            bumper.spend_turn()

    def position_on_level_map(self, (x, y)):  # for when player moves to to new depth of dungeon
        self.coord.set_position(x, y)
        self.set_position()
        # TODO if player has color source, add it to this map
        self.start_turn()

    def start_turn(self):
        self.game_state.ability_manager.update_panel_color()

    def spend_turn(self, free=False):
        self.turn_component.take_turn()
        self.level_map.game_state.ui.request_update()  # to update ability buttons

        self.game_state.ability_manager.update_panel_color()
        # clear any crystals used for free - we didn't use them
        self.level_map.game_state.ui.crystal_controller.reset_crystals(free=free)
