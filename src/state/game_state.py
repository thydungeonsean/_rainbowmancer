from abstract_state import AbstractState

from src.map.mapgen.level_gen import LevelGen

# components
from components.view import View
from components.view_port import ViewPort
from src.control.ui.ui import UI
from components.dungeon_input_handler import DungeonInputHandler
from components.player_controller import PlayerController

from src.game_object.player import Player


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

        self.level = None
        self.player = None

        self.view = None
        self.view_port = None

        self.initialize()

    def initialize(self):

        self.view = View(self)

        self.level = LevelGen.generate_level(self, 1, map_seed=None)

        self.view.set_new_map(self.level)
        self.view_port = ViewPort(self)

        self.player = Player(self.level)

        self.level.initialize(self.player)
        self.view.initialize()

    def new_level(self, depth, map_seed):

        self.level = LevelGen.generate_level(self, depth, map_seed)

        self.view.set_new_map(self.level)

        self.level.initialize(self.player)
        self.view.initialize()

    def initialize_ui(self):
        return UI(self)

    def initialize_input_handling(self):
        handler = DungeonInputHandler(self)
        return handler

    def draw(self):

        self.level.draw(self.view_port)

        self.view_port.draw(self.screen)

    def run(self):

        self.tick_frame()

        self.player_controller.run()
        self.level.run()

    def tick_frame(self):

        self.tick += 1

        if self.tick >= GameState.ANI_RATE:
            self.frame = GameState.NEXT_FRAME[self.frame]
            self.tick = 0
