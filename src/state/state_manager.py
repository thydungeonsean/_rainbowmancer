import sys
import pygame
from components.display_manager import DisplayManager
from src.enum.engine import *


class StateManager(object):

    def __init__(self, start_state):

        self.init()
        self.current_state = start_state(self)

    def init(self):

        pygame.init()
        display_manager = DisplayManager.get_instance()
        display_manager.initialize_display()

    def main(self):

        while self.current_state:
            complete = self.current_state.main()
            if complete:
                next_state_key = self.current_state.get_next_state()
                self.current_state = self.load_next_state(next_state_key)

        pygame.quit()
        sys.exit()

    @staticmethod
    def load_next_state(next_state):
        if next_state == EXIT_CODE:
            return None
        else:
            return next_state

    # add state loading functions to state manager
