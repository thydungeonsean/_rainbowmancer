

class PanelControl(object):

    def __init__(self, ui):

        self.ui = ui
        self.state = self.ui.state
        self.buttons = []

        self.load_buttons()

    @property
    def taking_input(self):
        return self.state.player_controller.ready

    def load_buttons(self):
        pass

    def deactivate_all(self):

        for button in self.buttons:
            button.button_component.deactivate()

    def click(self, key):
        pass

    def create_click_function(self, key_id):

        def click():
            self.click(key_id)

        return click

    def update(self):
        pass

    def request_update(self):
        self.ui.request_update()
