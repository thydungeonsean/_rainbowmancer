

class ColorSource(object):

    def __init__(self, level, hue, strength, coord):

        self.color_map = level
        self.hue = hue
        self.strength = strength
        self.coord = coord

        level.color_map.add_color_source(self)

    def move(self):
        self.color_map.request_recompute()
