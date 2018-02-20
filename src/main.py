import pygame
from state.state_manager import StateManager
from state.game_state import GameState


def main():

    pygame.init()
    game_state_manager = StateManager(GameState)
    game_state_manager.main()
