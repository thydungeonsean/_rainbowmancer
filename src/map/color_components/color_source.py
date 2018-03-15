

class ColorSource(object):

    def __init__(self, color_map, hue, strength, coord):

        self.color_map = color_map
        self.hue = hue
        self.strength = strength
        self.coord = coord

        self.color_map.add_color_source(self)

    def move(self):
        self.color_map.request_recompute()

    def kill(self):
        self.color_map.remove_color_source(self)
