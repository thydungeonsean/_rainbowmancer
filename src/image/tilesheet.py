import pygame
from src.enum.colors import *


class TileSheet(object):

    main_tilesheet = None
    icon_tilesheet = None

    @classmethod
    def get_tilesheet(cls):

        if cls.main_tilesheet is None:
            cls.main_tilesheet = cls('tilesheet')

        return cls.main_tilesheet.sheet

    @classmethod
    def get_icon_tilesheet(cls):

        if cls.icon_tilesheet is None:
            cls.icon_tilesheet = cls('icons')

        return cls.icon_tilesheet.sheet

    def __init__(self, sheet_id):

        self.sheet = pygame.image.load('assets/' + sheet_id + '.png').convert()

        pix_array = pygame.PixelArray(self.sheet)
        pix_array.replace(PURE_BLACK, BLACK)
        pix_array.replace(WHITE, START_COLOR)
