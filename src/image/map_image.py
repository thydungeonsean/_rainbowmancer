from src.config import *
from src.data_structures.vector import Vector
import pygame
from src.enum.colors import *
from src.image.image_cache import ImageCache


class MapImage(object):

    A = 0
    B = 1

    def __init__(self, level_map):

        assert level_map.tile_map

        self.level_map = level_map
        self.tile_map = self.level_map.tile_map
        self.state = self.level_map.game_state
        self.w = self.level_map.w
        self.h = self.level_map.h

        self.images = {
            (MapImage.A,): None,
            (MapImage.B,): None
        }

        self.coord = Vector(0, 0)

    def set_view_position(self):

        vx, vy = self.state.view.coord.position
        x = -vx * SCALE_TILE_W
        y = -vy * SCALE_TILE_H
        # print self.state.view.coord.position
        self.position((x, y))

    def position(self, (x, y)):
        self.coord.set_position(x, y)

    def draw(self, surface):
        surface.blit(self.images[(MapImage.A,)], self.coord.position)

    def create_map_image(self):

        image = pygame.Surface((self.w * SCALE_TILE_W, self.h * SCALE_TILE_H)).convert()
        image.fill(SHROUD)

        for x, y in self.tile_map.all_points:

            self.draw_tile((x, y), image)

        self.images[(MapImage.A,)] = image

    def draw_tile(self, (x, y), image):

        tile_id = self.tile_map.get_tile((x, y))
        tile_image = ImageCache.get_tile_image(tile_id)

        tile_image.position((x * SCALE_TILE_W, y * SCALE_TILE_H))
        tile_image.draw(image)



