

class Element(object):

    def __init__(self, ui, el_id=None):

        self.ui = ui
        self.element_id = el_id

        self.sub_elements = []

    def click(self, point):

        pass
