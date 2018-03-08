from image import Image, pygame
from src.config import *
from tilesheet import TileSheet
from tile_key import *
from src.enum.colors import *


class TileImage(Image):

    def __init__(self, tile_id, animated_frame=False):

        Image.__init__(self)

        self.tile_id = tile_id
        self.animated_frame = animated_frame

        self.load_tile_image()

    def load_tile_image(self):

        w = TILE_W
        h = TILE_H

        image = pygame.Surface((w, h))

        tilesheet = TileSheet.get_tilesheet()
        tx, ty = tile_key[self.tile_id]
        if self.animated_frame:
            ty += 1

        image.blit(tilesheet, (0, 0), (tx * w, ty * h, w, h))

        image = pygame.transform.scale(image, (SCALE_TILE_W, SCALE_TILE_H))
        image = image.convert()

        self.surface = image

        self.modify_wall()

    def modify_wall(self):

        if self.tile_id in WALLS:

            pix_array = pygame.PixelArray(self.surface)
            pix_array.replace(BLACK, LT_BLACK)
