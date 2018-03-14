from src.data_structures.vector import Vector


class Element(object):

    ids = 0

    def __init__(self, ui, w, h, coord=(0, 0), parent=None, el_id=None):

        self.ui = ui
        self.element_id = self.get_element_id(el_id)
        self.sub_elements = []
        self.components = []
        self.button_component = None  # a ref to the part of element that will be changed by clicking

        self.w = w
        self.h = h
        self.coord = Vector.from_tuple(coord)
        self.parent = self.set_parent(parent)

    @staticmethod
    def get_element_id(el_id):
        if el_id is None:
            el_id = Element.ids
            Element.ids += 1
        return el_id

    def add_child(self, child):
        self.sub_elements.append(child)

    def set_parent(self, parent):

        if parent is None:
            return None
        elif isinstance(parent, Element):
            parent.add_child(self)
            return parent
        elif isinstance(parent, basestring):
            p = self.ui.get_element(parent)
            p.add_child(self)
            return p

    def click(self, point):

        if self.point_is_over(point):
            self.on_click()
            for el in self.sub_elements:
                el.click(point)

    def on_click(self):
        pass

    def point_is_over(self, (x, y)):

        sx, sy = self.screen_coord
        return sx <= x < sx + self.w and sy <= y < sy + self.h

    @property
    def screen_coord(self):
        if self.parent is not None:
            px, py = self.parent.screen_coord
        else:
            px, py = 0, 0
        x, y = self.coord.int_position
        return x + px, y + py

    def draw(self, surface):

        for component in self.components:
            component.draw(surface)

        for element in self.sub_elements:
            element.draw(surface)

    def run(self):

        for component in self.components:
            component.run()

    def add_component(self, component):
        self.components.append(component)

    def add_component_as_button(self, component):
        self.add_component(component)
        self.button_component = component
