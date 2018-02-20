import math
from src.config import SCALE


class Vector(object):

    @classmethod
    def scaled(cls, x, y):
        vec = cls(x, y)
        vec.set_scaled_flag()
        return vec

    @classmethod
    def from_tuple(cls, (x, y)):
        return cls(x, y)

    @classmethod
    def from_angle(cls, angle):
        _angle = math.radians(angle)
        x = math.cos(_angle)
        y = math.sin(_angle)
        return cls(x, y)

    def __init__(self, x, y):
        x, y = self.enforce_type(x, y)

        self.x = x
        self.y = y
        self.scaled = False

    @property
    def position(self):
        return self.x, self.y

    @property
    def int_position(self):
        return int(round(self.x)), int(round(self.y))

    def enforce_type(self, x, y):
        return float(x), float(y)

    def set_position(self, x, y):
        x, y = self.enforce_type(x, y)
        self.x = x
        self.y = y

    def set_from_tuple(self, (x, y)):
        self.set_position(x, y)

    def normalize(self):
        # TODO make the normalize vector func
        return

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

    def sub(self, vec):
        self.x -= vec.x
        self.y -= vec.y

    def mult(self, factor):
        self.x *= factor
        self.y *= factor

    def div(self, divisor):
        self.x = self.x / divisor
        self.y = self.y / divisor

    def scale(self):
        self.mult(SCALE)
        self.set_scaled_flag()

    def set_scaled_flag(self):
        self.scaled = True

        def blank():
            pass
        self.scale = blank
