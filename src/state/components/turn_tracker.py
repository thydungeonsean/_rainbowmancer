from state_component import StateComponent


class TurnTracker(StateComponent):

    PLAYER_TURN = 127
    MONSTER_TURN = 126

    def __init__(self, state):

        StateComponent.__init__(self, state)

        self.active_turn = TurnTracker.PLAYER_TURN

    @property
    def is_player_turn(self):
        return self.active_turn == TurnTracker.PLAYER_TURN

    @property
    def is_monster_turn(self):
        return self.active_turn == TurnTracker.MONSTER_TURN

    def reset(self):
        self.active_turn = TurnTracker.PLAYER_TURN

    def end_player_turn(self):

        self.active_turn = TurnTracker.MONSTER_TURN
        self.state.player_controller.block_player_input()

    def end_monster_turn(self):

        self.active_turn = TurnTracker.PLAYER_TURN
        self.state.player_controller.release_player_input()

        # refresh turn components
        self.state.level.object_manager.refresh_turn_components()
        self.state.level.player.start_turn()

    def run(self):

        if self.is_player_turn:
            if not self.state.player.ready:
                self.end_player_turn()
        elif self.is_monster_turn:
            pass
            # TODO
            # if all monsters are done, end their turn
