import pygame
from components.display_manager import DisplayManager
from src.control.event_handling.input_handler import InputHandler
from src.enum.engine import *
from src.config import *


class AbstractState(object):

    def __init__(self, state_manager):

        self.state_manager = state_manager
        self.next_state = EXIT_CODE
        self.exit_state = False

        self.screen = DisplayManager.get_instance().get_screen_surface()

        self.clock = pygame.time.Clock()

        # state components
        self.ui = self.initialize_ui()
        self.input_handler = self.initialize_input_handling()

    ##########
    # ui
    def initialize_ui(self):
        raise NotImplementedError

    ##########
    # input initialization
    def initialize_input_handling(self):
        handler = InputHandler(self)
        return handler

    ##########
    # state transition methods
    def set_next_state(self, next_state):
        self.next_state = next_state

    def get_next_state(self):
        return self.next_state

    def trigger_exit(self):
        self.exit_state = True

    def reset_state(self):
        self.set_next_state(EXIT_CODE)
        self.exit_state = False

    def exit_game(self):
        self.set_next_state(EXIT_CODE)
        self.trigger_exit()

    ##########
    # main loop methods
    def main(self):

        while True:

            if self.exit_state:
                return True

            self.handle_input()

            self.run()

            self.draw()
            pygame.display.update()

            self.clock.tick(FPS)

    def handle_input(self):
        self.input_handler.handle_input()

    def run(self):
        pass

    def draw(self):
        raise NotImplementedError
