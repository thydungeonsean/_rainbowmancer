from src.enum.stat_keys import create_monster, monster_stats
from src.enum.hues import *


monsters = {

    'gnome': create_monster(
                name='gnome',
                depth_rng=(1, 10)),

    'naga': create_monster(
                name='naga',
                # image=NAGA,
                max_health=4,
                atk=2,
                color_component=BLUE_HUE,
                depth_rng=(2, 5)),




}