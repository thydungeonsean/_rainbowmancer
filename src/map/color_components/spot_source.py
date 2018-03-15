

class SpotColorSource(object):

    def __init__(self, color_map, hue, coord):

        self.color_map = color_map
        self.hue = hue
        self.coord = coord  # just a tuple

        self.color_map.add_spot_color_source(self)

    def move(self):
        self.color_map.request_recompute()

    def kill(self):
        self.color_map.remove_spot_color_source(self)
