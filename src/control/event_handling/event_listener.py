

class EventListener(object):

    def __init__(self, key_code, key_down=None, key_up=None):

        self.input_handler = None
        self.key_code = key_code

        if key_down is not None:
            self.key_down = key_down
        if key_up is not None:
            self.key_up = key_up

    def set_input_handler(self, handler):
        self.input_handler = handler

    @property
    def state(self):
        return self.input_handler.state

    def key_down(self):
        pass

    def key_up(self):
        pass

    def exit_game(self):
        self.input_handler.state.exit_game()

    def set_key_down_function(self, f):
        self.key_down = f

    def set_key_up_function(self, f):
        self.key_up = f
