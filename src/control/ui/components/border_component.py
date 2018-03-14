from element_component import ElementComponent
from src.image.image_cache import ImageCache
import pygame
from src.config import *
from src.enum.ui import *


class BorderComponent(ElementComponent):

    TL = 0
    TR = 1
    BL = 2
    BR = 3
    T = 4
    S = 5

    style_1 = {TL: BORDER_1_TL, TR: BORDER_1_TR, BL: BORDER_1_BL, BR: BORDER_1_BR, T: BORDER_1_T, S: BORDER_1_S}
    style_2 = {TL: BORDER_2_TL, TR: BORDER_2_TR, BL: BORDER_2_BL, BR: BORDER_2_BR, T: BORDER_2_T, S: BORDER_2_S}

    borders = {1: style_1, 2: style_2}

    def __init__(self, owner, style=1):

        ElementComponent.__init__(self, owner)
        self.style = style
        self.surface = self.create_border_image()

    @property
    def w(self):
        return self.owner.w

    @property
    def h(self):
        return self.owner.h

    def create_border_image(self):

        surface = pygame.Surface((self.w, self.h)).convert()

        if self.w < TILE_W*2 or self.h < TILE_H * 2:
            return surface

        self.draw_sides(surface)
        self.draw_corners(surface)

        return surface

    def draw(self, surface):

        surface.blit(self.surface, self.owner.screen_coord)

    def draw_corners(self, surface):

        borders = BorderComponent.borders[self.style]

        tile = ImageCache.get_ui_tile_image(borders[BorderComponent.TL])
        tile.draw(surface)

        tile = ImageCache.get_ui_tile_image(borders[BorderComponent.TR])
        tile.position((self.w-TILE_W, 0))
        tile.draw(surface)

        tile = ImageCache.get_ui_tile_image(borders[BorderComponent.BL])
        tile.position((0, self.h-TILE_H))
        tile.draw(surface)

        tile = ImageCache.get_ui_tile_image(borders[BorderComponent.BR])
        tile.position((self.w-TILE_W, self.h-TILE_H))
        tile.draw(surface)

    def draw_sides(self, surface):

        borders = BorderComponent.borders[self.style]

        top_w = self.w - TILE_W * 2

        tile = ImageCache.get_ui_tile_image(borders[BorderComponent.T])

        for x in range(top_w/TILE_W):
            tile.position(((x * TILE_W)+TILE_W, 0))
            tile.draw(surface)
            tile.position(((x * TILE_W) + TILE_W, self.h - TILE_H))
            tile.draw(surface)

        side_w = self.h - TILE_H * 2

        tile = ImageCache.get_ui_tile_image(borders[BorderComponent.S])

        for y in range(side_w/TILE_H):
            tile.position((0, (y * TILE_H)+TILE_H))
            tile.draw(surface)
            tile.position((self.w - TILE_W, (y * TILE_H) + TILE_H))
            tile.draw(surface)
