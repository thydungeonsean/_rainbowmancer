from game_object import GameObject


class Exit(GameObject):

    def __init__(self, level_map, coord, depth):

        GameObject.__init__(self, level_map, coord, True, True)

        self.depth = depth

    def on_bump(self):

        print 'go down the dungeon!'
        self.level_map.game_state.new_level(self.depth, self.level_map.map_seed+1)
