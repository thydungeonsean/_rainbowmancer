from ability import Ability
from src.enum.hues import *


class Invoke(Ability):

    def __init__(self, manager):

        Ability.__init__(self, manager)

    def can_be_cast(self):
        return self.panel.ability_color != WHITE_HUE
