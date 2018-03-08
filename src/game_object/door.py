from game_object import GameObject


class Door(GameObject):

    CLOSED = 0
    OPEN = 1

    def __init__(self, level_map, coord):

        GameObject.__init__(self, level_map, coord, True, True)

        self.state = Door.CLOSED

    def on_bump(self):

        if self.state == Door.CLOSED:
            self.open_door()

    def open_door(self):

        self.state = Door.OPEN
        self.blocks = False
        self.block_sight = False

        # TODO change tile of tile_map
