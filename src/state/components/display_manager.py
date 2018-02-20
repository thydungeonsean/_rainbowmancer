import os
import pygame
from src.enum.engine import *
from src.config import *


class DisplayManager(object):

    instance = None

    @classmethod
    def get_instance(cls):

        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    def __init__(self):

        self.fullscreen = FULLSCREEN_ON

    def initialize_display(self):

        os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
        self.set_display_mode()

    def set_display_mode(self):

        if self.fullscreen:
            pygame.display.set_mode((SCALE_SCREEN_W, SCALE_SCREEN_H), FULLSCREEN)
        else:
            pygame.display.set_mode((SCALE_SCREEN_W, SCALE_SCREEN_H))

    def toggle_fullscreen(self):

        if self.fullscreen:
            self.fullscreen = False
        else:
            self.fullscreen = True

        self.set_display_mode()

    def get_screen_surface(self):

        return pygame.display.get_surface()
