from src.enum.stat_keys import create_monster, monster_stats
from src.enum.hues import *
from src.enum.objects import *


monsters = {

    # neutral
    'gnome': create_monster(
                name='gnome',
                depth_rng=(1, 10)),

    # blue
    'naga': create_monster(
                name='naga',
                image=NAGA,
                max_health=4,
                atk=2,
                color_component=BLUE_HUE,
                depth_rng=(2, 5)),

    # green
    'centaur': create_monster(
                name='centaur',
                image=CENTAUR,
                max_health=5,
                atk=1,
                color_component=GREEN_HUE,
                depth_rng=(1, 7)),

    # red


    # yellow
    'skeleton': create_monster(
                name='skeleton',
                image=SKELETON,
                max_health=2,
                atk=2,
                color_component=YELLOW_HUE,
                depth_range=(2, 8)),

    'skeleton_archer': create_monster(
                name='skeleton archer',
                image=SKELETON_ARCHER,
                max_health=2,
                atk=1,
                color_component=YELLOW_HUE,
                depth_range=(4, 10)),

    # cyan
    'fae': create_monster(
                name='fae',
                image=FAE,
                atk=1,
                color_component=CYAN_HUE,
                depth_range=(5, 14)),

    # purple
    'dark_elf': create_monster(
                name='dark elf',
                image=DARK_ELF,
                atk=3,
                max_health=4,
                color_component=PURPLE_HUE,
                depth_range=(8, 16)),

}