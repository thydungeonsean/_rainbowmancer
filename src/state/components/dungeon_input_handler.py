from src.control.event_handling.input_handler import InputHandler
from src.control.event_handling.event_listener import EventListener
from src.enum.engine import *


class DungeonInputHandler(InputHandler):

    def __init__(self, state):

        exit_func = EventListener(K_ESCAPE, key_down=state.exit_game)

        up = EventListener(K_UP, key_down=state.view_controller.press_up,
                           key_up=state.view_controller.release_up)
        down = EventListener(K_DOWN, key_down=state.view_controller.press_down,
                             key_up=state.view_controller.release_down)
        left = EventListener(K_LEFT, key_down=state.view_controller.press_left,
                             key_up=state.view_controller.release_left)
        right = EventListener(K_RIGHT, key_down=state.view_controller.press_right,
                              key_up=state.view_controller.release_right)

        InputHandler.__init__(self, state, exit_func, up, down, left, right)

    def on_mouse_motion(self):
        pass
