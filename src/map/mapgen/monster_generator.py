from src.game_object.actor_stats import monster_archive
from src.game_object.enemy import Enemy
from random import choice


class MonsterGenerator(object):

    instance = None

    @classmethod
    def get_instance(cls):

        if not cls.instance:
            cls.instance = cls()

        return cls.instance

    def __init__(self):

        pass

    def spawn_monsters(self, level, coords):

        for coord in coords:
            monster = self.get_monster_for_depth(level, coord)
            level.add_object(monster)

    def get_monster_for_depth(self, level, coord):

        actor_id = self.choose_monster_type(level, coord)

        return Enemy(level, coord, actor_id)

    def choose_monster_type(self, level, coord):

        return choice(monster_archive.monsters.keys())
