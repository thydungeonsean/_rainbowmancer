from image import Image, pygame
from src.config import *
from tilesheet import TileSheet
from tile_key import *


class TileImage(Image):

    def __init__(self, tile_id):

        Image.__init__(self)
        self.tile_id = tile_id

        self.load_tile_image()

    def load_tile_image(self):

        w = TILE_W
        h = TILE_H

        image = pygame.Surface((w, h))

        tilesheet = TileSheet.get_tilesheet()
        tx, ty = tile_key[self.tile_id]

        image.blit(tilesheet, (0, 0), (tx * w, ty * h, w, h))
        image = image.convert()

        self.surface = image
