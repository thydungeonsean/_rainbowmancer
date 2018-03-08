from src.data_structures.vector import Vector
from src.enum.colors import *
import pygame


class Image(object):

    def __init__(self):

        self.surface = None
        self.coord = Vector(0, 0)
        self.color_id = START_COLOR

    def position(self, (x, y)):

        self.coord.set_position(x, y)

    def draw(self, surface):

        surface.blit(self.surface, self.coord.position)

    def change_color(self, new_color):
        pixel_array = pygame.PixelArray(self.surface)
        pixel_array.replace(self.color_id, new_color)
        self.color_id = new_color

    @property
    def w(self):
        return self.surface.get_width()

    @property
    def h(self):
        return self.surface.get_height()
