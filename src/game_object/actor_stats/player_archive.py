from src.enum.stat_keys import create_player, player_stats
from src.enum.hues import *
from src.image.tile_key import *


players = {

    'test': create_player(
                    name="rainbowmancer",
                    image=RAINBOWMANCER,
                    max_health=100),

    'rainbowmancer': create_player(),

    'cyan knight': create_player(
                    name="cyan knight",
                    image=CYAN_KNIGHT,
                    max_health=5,
                    atk=2,
                    color_component=CYAN_HUE,
                    ability_list=['summon', 'wall', 'shatter', 'imbue'])
}
