from src.image.tile_key import *


REFLECT_COMPONENT = -1


player_stats = ['name', 'image', 'max_health', 'atk', 'color_component', 'color_source', 'source_rng',
                'ability_list', 'actor_class']

default_player = {
    'name': 'rainbowmancer',
    'image': RAINBOWMANCER,
    'max_health': 3,
    'atk': 1,
    'color_component': REFLECT_COMPONENT,
    'color_source': False,
    'source_rng': 3,
    'ability_list': ['bind', 'summon', 'bolt', 'ray', 'wall', 'shatter', 'imbue'],
    'actor_class': 'player'
}


def create_player(**kwargs):
    stats = {}
    for s in player_stats:
        stats[s] = kwargs.get(s, default_player[s])

    return stats


###################################################################################
# Monster stats

monster_stats = ['name', 'image', 'max_health', 'atk', 'color_component', 'color_source', 'source_rng',
                 'ai_type', 'ability', 'depth_rng', 'actor_class']

default_monster = {
    'name': 'bad boy',
    'image': GNOME,
    'max_health': 3,
    'atk': 1,
    'color_component': REFLECT_COMPONENT,
    'color_source': False,
    'source_rng': 3,
    'ai_type': 'random_walk',
    'ability': None,
    'depth_rng': (1, 3),
    'actor_class': 'monster'
}


def create_monster(**kwargs):

    stats = {}
    for s in monster_stats:
        stats[s] = kwargs.get(s, default_monster[s])

    return stats
