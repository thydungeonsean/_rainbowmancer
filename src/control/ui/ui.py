from src.state.components.state_component import StateComponent


class UI(StateComponent):

    def __init__(self, state):

        StateComponent.__init__(self, state)

        self.elements = []
        self.key_element_dict = {}

    def draw(self, surface):

        for element in self.elements:
            element.draw(surface)

    # membership methods
    def add_element(self, element):
        self.elements.append(element)

    def remove_element(self, element):
        self.elements.remove(element)

    def add_key_element(self, element, key):
        self.add_element(element)
        self.key_element_dict[key] = element

    def get_key_element(self, key):
        return self.key_element_dict[key]

    def remove_key_element(self, key):
        element = self.key_element_dict[key]
        del self.key_element_dict[key]
        self.remove_element(element)

    # handle clicking ui elements
    def click(self, pos):
        for element in self.elements:
            element.click(pos)

    def right_click(self, pos):
        for element in self.elements:
            element.click(pos)
