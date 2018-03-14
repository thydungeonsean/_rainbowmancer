from state_component import StateComponent
import pygame
from src.config import *
from view import View


class ViewPort(StateComponent):

    W = View.VIEW_W * SCALE_TILE_W
    H = View.VIEW_H * SCALE_TILE_H

    coord = 0, 0

    def __init__(self, state):

        StateComponent.__init__(self, state)
        cls = ViewPort
        self.surface = pygame.Surface((cls.W, cls.H)).convert()
        self.coord = ViewPort.coord

    @property
    def view(self):
        return self.state.view

    def draw(self, surface):

        surface.blit(self.surface, self.coord)
