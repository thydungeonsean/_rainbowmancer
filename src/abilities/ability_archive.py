from src.enum.abilities import *
from ability import Ability
from bolt import Bolt
from bind import Bind
from summon import Summon
from block import Block
from ray import Ray
from shatter import Shatter
from invoke import Invoke
from imbue import Imbue


class AbilityArchive(object):

    def __init__(self, manager):

        self.manager = manager
        self.abilities = {
            BOLT: Bolt(self.manager),
            BIND: Bind(self.manager),
            SUMMON: Summon(self.manager),
            BLOCK: Block(self.manager),
            IMBUE: Imbue(self.manager),
            INVOKE: Invoke(self.manager),
            RAY: Ray(self.manager),
            SHATTER: Shatter(self.manager),
        }

    def get_ability(self, key):

        return self.abilities[ability_string_to_id[key]]
