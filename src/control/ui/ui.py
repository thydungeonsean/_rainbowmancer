from src.state.components.state_component import StateComponent


class UI(StateComponent):

    def __init__(self, state):

        StateComponent.__init__(self, state)

        self.elements = {}
        self.controllers = []

        self.needs_update = True

    def run(self):
        for element in self.elements.itervalues():
            element.run()
        if self.needs_update:
            self.update_controllers()

    def draw(self, surface):

        for element in self.elements.itervalues():
            if element.parent is None:
                element.draw(surface)

    # membership methods
    def add_element(self, element):
        self.elements[element.element_id] = element

    def remove_element(self, element):
        del self.elements[element.element_id]

    def get_element(self, key):
        return self.elements[key]

    def add_controller(self, controller):
        self.controllers.append(controller)

    # handle clicking ui elements
    def click(self, pos):
        for element in self.elements.itervalues():
            if element.parent is None:
                element.click(pos)

    def right_click(self, pos):
        for element in self.elements.itervalues():
            if element.parent is None:
                element.click(pos)

    def request_update(self):
        self.needs_update = True

    def update_controllers(self):

        for controller in self.controllers:
            controller.update()

        self.needs_update = False
