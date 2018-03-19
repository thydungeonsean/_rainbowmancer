from game_object import GameObject


class Exit(GameObject):

    def __init__(self, level_map, coord, depth):

        GameObject.__init__(self, level_map, coord, True, True)

        self.obj_id = 'exit'
        self.depth = depth

    def on_bump(self, bumper):

        print 'go down the dungeon!'
        if bumper.team == "PLAYER":
            self.level_map.game_state.new_level(self.depth, self.level_map.map_seed+1)
