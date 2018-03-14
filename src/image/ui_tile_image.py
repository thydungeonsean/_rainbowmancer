from tile_image import TileImage
from src.config import *
import pygame
from tilesheet import TileSheet
from tile_key import *
from src.enum.colors import *


class UITileImage(TileImage):

    def __init__(self, tile_id):

        TileImage.__init__(self, tile_id)

    def load_tile_image(self):

        w = TILE_W
        h = TILE_H

        image = pygame.Surface((w, h))

        tilesheet = TileSheet.get_tilesheet()
        tx, ty = tile_key[self.tile_id]

        image.blit(tilesheet, (0, 0), (tx * w, ty * h, w, h))

        image = image.convert()

        self.surface = image

        self.change_ui_colors()

    def change_ui_colors(self):

        pix_array = pygame.PixelArray(self.surface)
        pix_array.replace(BLACK, PURE_BLACK)
        pix_array.replace(GREY_1, WHITE)

