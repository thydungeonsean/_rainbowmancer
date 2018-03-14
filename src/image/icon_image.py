from tile_image import TileImage
from src.config import *
from tilesheet import TileSheet
import pygame
from tile_key import *
from src.enum.colors import *


class IconImage(TileImage):

    def __init__(self, image_id):

        TileImage.__init__(self, image_id)

    def load_tile_image(self):

        w = ICON_W
        h = ICON_H

        image = pygame.Surface((w, h))

        tilesheet = TileSheet.get_icon_tilesheet()
        tx, ty = tile_key[self.tile_id]

        image.blit(tilesheet, (0, 0), (tx * w, ty * h, w, h))

        image = image.convert()

        pix_array = pygame.PixelArray(image)
        pix_array.replace(BLACK, PURE_BLACK)
        pix_array.replace(GREY_1, WHITE)
        self.color_id = WHITE

        self.surface = image
