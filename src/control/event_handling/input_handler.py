from src.state.components.state_component import StateComponent
import pygame
from pygame.locals import *


class InputHandler(StateComponent):

    LEFT_MOUSE_BUTTON = 1
    RIGHT_MOUSE_BUTTON = 3

    def __init__(self, state, *args):

        StateComponent.__init__(self, state)
        self.event_listeners = {}
        self.active_key_codes = set()

        for listener in args:
            self.add_event_listener(listener)

    def handle_input(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.state.trigger_exit()

            elif event.type == KEYDOWN:

                if event.key in self.active_key_codes:
                    self.event_listeners.get(event.key).key_down()

            elif event.type == KEYUP:

                if event.key in self.active_key_codes:
                    self.event_listeners.get(event.key).key_up()

            elif event.type == MOUSEBUTTONDOWN:

                if event.button == InputHandler.LEFT_MOUSE_BUTTON:
                    self.on_left_click()

                elif event.button == InputHandler.RIGHT_MOUSE_BUTTON:
                    self.on_right_click()

            elif event.type == MOUSEMOTION:
                self.on_mouse_motion()

    def add_event_listener(self, listener):

        code = listener.key_code
        self.event_listeners[code] = listener
        self.active_key_codes.add(code)
        listener.set_input_handler(self)

    def on_left_click(self):
        self.state.ui.click(pygame.mouse.get_pos())

    def on_right_click(self):
        self.state.ui.right_click(pygame.mouse.get_pos())

    def on_mouse_motion(self):
        pass
