from actor import Actor


class Player(Actor):

    def __init__(self, level_map, coord):

        Actor.__init__(self, level_map, coord, 'rainbowmancer')

    def on_move(self):
        self.level_map.fov_map.recompute_fov()
