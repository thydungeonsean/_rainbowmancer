from src.control.event_handling.input_handler import InputHandler
from src.control.event_handling.event_listener import EventListener
from src.enum.engine import *


class DungeonInputHandler(InputHandler):

    def __init__(self, state):

        exit_func = EventListener(K_ESCAPE, key_down=state.exit_game)

        up = EventListener(K_UP, key_down=state.player_controller.press_up,
                           key_up=state.player_controller.release_up)
        down = EventListener(K_DOWN, key_down=state.player_controller.press_down,
                             key_up=state.player_controller.release_down)
        left = EventListener(K_LEFT, key_down=state.player_controller.press_left,
                             key_up=state.player_controller.release_left)
        right = EventListener(K_RIGHT, key_down=state.player_controller.press_right,
                              key_up=state.player_controller.release_right)

        alt_up = EventListener(K_w, key_down=state.player_controller.press_up,
                               key_up=state.player_controller.release_up)
        alt_down = EventListener(K_s, key_down=state.player_controller.press_down,
                                 key_up=state.player_controller.release_down)
        alt_left = EventListener(K_a, key_down=state.player_controller.press_left,
                                 key_up=state.player_controller.release_left)
        alt_right = EventListener(K_d, key_down=state.player_controller.press_right,
                                  key_up=state.player_controller.release_right)

        InputHandler.__init__(self, state, exit_func, up, down, left, right, alt_up, alt_down, alt_left, alt_right)

    def on_mouse_motion(self):
        pass
