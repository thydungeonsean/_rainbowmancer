from game_object_component import GameObjectComponent
from src.game_object.actor_stats import monster_archive
from src.game_object.actor_stats import player_archive
from src.sound.sounds import *


class StatComponent(GameObjectComponent):

    def __init__(self, owner, stat_key):

        GameObjectComponent.__init__(self, owner)
        self.stat_key = stat_key

        self.stats = {}
        self.load_stats()

        self.dead = False

    @property
    def critical(self):
        return self.stats['health'] == 1 and self.stats['max_health'] != 1

    def load_stats(self):

        if self.stat_key in player_archive.players:
            self.load_player_stats()

        else:
            self.load_monster_stats()

        self.stats['health'] = self.stats['max_health']

    def load_player_stats(self):

        for stat in player_archive.player_stats:
            self.stats[stat] = player_archive.players[self.stat_key][stat]

    def load_monster_stats(self):

        for stat in monster_archive.monster_stats:
            self.stats[stat] = monster_archive.monsters[self.stat_key][stat]

    @property
    def image_id(self):
        return self.stats['image']

    def attack(self, foe):

        if not foe.dead:
            dmg = self.stats['atk']
            foe.stat_component.take_damage(dmg)

    def take_damage(self, dmg):

        self.stats['health'] -= dmg
        if self.stats['health'] <= 0:
            self.dead = True
            # TODO death sound
            self.die()

        else:
            SoundArchive.get_instance().play_sound('hit1')

    def die(self):
        self.dead = True
        self.owner.level_map.object_manager.request_update()
