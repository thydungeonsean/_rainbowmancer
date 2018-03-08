from src.control.event_handling.arrow_key_controller import ArrowKeyController


class PlayerController(ArrowKeyController):

    HOLD_DELAY = 15

    def __init__(self, state):

        ArrowKeyController.__init__(self)
        self.state = state

        self.ready = True
        self.key_pressed = False
        self.key_active = False

        self.hold_down_timer = 0

    @property
    def player(self):
        return self.state.player

    @property
    def holding(self):
        return self.hold_down_timer > PlayerController.HOLD_DELAY

    def run(self):

        if self.ready and self.key_pressed and self.key_active:
            self.move_player(self.vector)
            self.key_active = False

            if not self.holding:
                self.hold_down_timer = 0
            else:
                self.hold_down_timer = PlayerController.HOLD_DELAY - 2

        if self.key_pressed:
            self.hold_down_timer += 1
            if self.hold_down_timer > PlayerController.HOLD_DELAY:
                self.key_active = True

        else:
            self.key_active = False
            self.hold_down_timer = 0

    def on_press(self):
        self.key_pressed = True
        self.key_active = True

    def on_release(self):
        self.key_pressed = False

    def move_player(self, vector):

        self.player.try_move(vector)
        self.state.view.set_view_position()
        self.player.set_position()
