from game_object_component import GameObjectComponent
from src.game_object.actor_stats import monster_archive
from src.game_object.actor_stats import player_archive


class StatComponent(GameObjectComponent):

    def __init__(self, owner, stat_key):

        GameObjectComponent.__init__(self, owner)
        self.stat_key = stat_key

        self.stats = {}
        self.load_stats()

        self.dead = False

    def load_stats(self):

        if self.stat_key in player_archive.players:
            self.load_player_stats()

        else:
            self.load_monster_stats()

    def load_player_stats(self):

        for stat in player_archive.player_stats:
            self.stats[stat] = player_archive.players[self.stat_key][stat]

    def load_monster_stats(self):

        for stat in monster_archive.monster_stats:
            self.stats[stat] = monster_archive.monsters[self.stat_key][stat]

    @property
    def image_id(self):
        return self.stats['image']
