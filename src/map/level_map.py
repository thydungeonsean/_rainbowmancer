

class LevelMap(object):

    def __init__(self):

        self.terrain_map = None
        self.tile_map = None
        self.color_map = None
        self.fov_map = None

    @property
    def w(self):
        return self.terrain_map.w

    @property
    def h(self):
        return self.terrain_map.h