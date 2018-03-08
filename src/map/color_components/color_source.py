

class ColorSource(object):

    def __init__(self, color_map, hue, strength, coord):

        self.color_map = color_map
        self.hue = hue
        self.strength = strength
        self.coord = coord

    def move(self, new):
        self.coord = new
        self.color_map.request_recompute()