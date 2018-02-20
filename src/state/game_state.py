from abstract_state import AbstractState

# components
from components.view_controller import ViewController
from src.control.ui.ui import UI
from components.dungeon_input_handler import DungeonInputHandler


class GameState(AbstractState):

    def __init__(self, state_manager):

        self.view_controller = ViewController(self)
        AbstractState.__init__(self, state_manager)

        # self.terrain_map = TerrainMap(50, 40)
        # self.terrain_map.random_map()

        self.initialize()

    def initialize(self):
        pass

    def initialize_ui(self):
        return UI(self)

    def initialize_input_handling(self):
        handler = DungeonInputHandler(self)
        return handler

    def draw(self):

        pass

    def run(self):
        self.view_controller.run()
