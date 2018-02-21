from _map import _Map


class SubMap(_Map):

    def __init__(self, w, h, level_map):

        _Map.__init__(self, w, h)
        self.level_map = level_map

    @property
    def color_map(self):
        return self.level_map.color_map

    @property
    def fov_map(self):
        return self.level_map.fov_map

    @property
    def terrain_map(self):
        return self.level_map.terrain_map
