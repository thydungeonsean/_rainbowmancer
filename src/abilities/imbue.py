from ability import Ability
from src.enum.hues import *


class Imbue(Ability):

    def __init__(self, manager):

        Ability.__init__(self, manager)

    def can_be_cast(self):
        # TODO if white hue, specific conditions must be met to rest

        return True
