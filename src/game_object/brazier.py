from game_object import GameObject


class Brazier(GameObject):

    def __init__(self, level_map, coord):

        GameObject.__init__(self, level_map, coord, False, True)

        # TODO check it's tile, if lit use the animated and add color_source etc.

    def on_bump(self):

        print 'bump brazier'
