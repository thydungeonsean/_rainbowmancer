from src.control.event_handling.arrow_key_controller import ArrowKeyController


class ViewController(ArrowKeyController):

    def __init__(self, state):

        ArrowKeyController.__init__(self)
        self.state = state
        self.speed = 16

    def run(self):

        if self.pressed[ViewController.UP]:
            y = self.speed
        elif self.pressed[ViewController.DOWN]:
            y = -self.speed
        else:
            y = 0

        if self.pressed[ViewController.LEFT]:
            x = self.speed
        elif self.pressed[ViewController.RIGHT]:
            x = -self.speed
        else:
            x = 0

        self.vector.set_position(x, y)

        # self.state.view.move_view(self.vector)
