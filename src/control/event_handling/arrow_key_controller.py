from src.data_structures.vector import Vector


class ArrowKeyController(object):

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    DIRECTIONS = {UP, RIGHT, DOWN, LEFT}
    STR_DIRECTIONS = {'up': UP, 'right': RIGHT, 'down': DOWN, 'left': LEFT}

    def __init__(self):

        cls = ArrowKeyController
        self.pressed = {cls.UP: False, cls.DOWN: False, cls.LEFT: False, cls.RIGHT: False}
        self.vector = Vector(0, 0)

    def press(self, k_id):
        cls = ArrowKeyController
        if k_id in cls.DIRECTIONS:
            self.pressed[k_id] = True
        # elif k_id.lower() in cls.STR_DIRECTIONS:
        #     self.pressed[cls.STR_DIRECTIONS[k_id]] = True
        else:
            raise Exception('invalid key code')

    def release(self, k_id):
        cls = ArrowKeyController
        if k_id in cls.DIRECTIONS:
            self.pressed[k_id] = False
        # elif k_id.lower() in cls.STR_DIRECTIONS:
        #     self.pressed[cls.STR_DIRECTIONS[k_id]] = False
        else:
            raise Exception('invalid key code')

    def press_up(self):
        cls = ArrowKeyController
        self.press(cls.UP)

    def release_up(self):
        cls = ArrowKeyController
        self.release(cls.UP)

    def press_down(self):
        cls = ArrowKeyController
        self.press(cls.DOWN)

    def release_down(self):
        cls = ArrowKeyController
        self.release(cls.DOWN)

    def press_left(self):
        cls = ArrowKeyController
        self.press(cls.LEFT)

    def release_left(self):
        cls = ArrowKeyController
        self.release(cls.LEFT)

    def press_right(self):
        cls = ArrowKeyController
        self.press(cls.RIGHT)

    def release_right(self):
        cls = ArrowKeyController
        self.release(cls.RIGHT)