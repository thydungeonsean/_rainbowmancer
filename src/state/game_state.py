from abstract_state import AbstractState

# components
from components.view import View
from components.view_port import ViewPort
from src.control.ui.ui import UI
from components.dungeon_input_handler import DungeonInputHandler
from components.player_controller import PlayerController

# test
from src.map.mapgen.cave_map_generator import CaveMapGen
from src.map.level_map import LevelMap
from src.map.tile_map import TileMap
from src.image.map_image import MapImage

from src.game_object.player import Player


def badbad(s):

    level = LevelMap(s)
    level.terrain_map = CaveMapGen.generate_cave_terrain_map(50, 20)
    level.terrain_map.level_map = level
    level.tile_map = TileMap(level)
    level.tile_map.initialize()

    level.map_image = MapImage(level)

    level.map_image.create_map_image()

    return level


class GameState(AbstractState):

    A = 0
    B = 1

    NEXT_FRAME = {A: B, B: A}

    ANI_RATE = 15

    def __init__(self, state_manager):

        self.player_controller = PlayerController(self)
        AbstractState.__init__(self, state_manager)

        self.frame = GameState.A
        self.tick = 0

        # self.terrain_map = TerrainMap(50, 40)
        # self.terrain_map.random_map()

        self.level = None
        self.player = None

        self.view = None
        self.view_port = None

        self.initialize()

    def initialize(self):

        self.screen.fill((200, 100, 0))

        self.level = badbad(self)

        self.view = View(self, self.level.w, self.level.h)
        self.view_port = ViewPort(self)

        self.player = Player(self.level, self.level.entrance)
        self.view.initialize()

        self.level.add_player(self.player)

    def initialize_ui(self):
        return UI(self)

    def initialize_input_handling(self):
        handler = DungeonInputHandler(self)
        return handler

    def draw(self):

        self.level.draw(self.view_port)

        self.view_port.draw(self.screen)

    def run(self):
        self.player_controller.run()
        self.level.map_image.set_view_position()
        self.tick_frame()

    def tick_frame(self):

        self.tick += 1

        if self.tick >= GameState.ANI_RATE:
            self.frame = GameState.NEXT_FRAME[self.frame]
            self.tick = 0
