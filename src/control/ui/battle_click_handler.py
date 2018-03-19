from src.config import *


class BattleClickHandler(object):

    def __init__(self, ui):

        self.ui = ui
        self.state = ui.state

    @property
    def ready(self):
        return self.state.player_controller.ready

    @property
    def active_ability(self):
        return self.state.ability_manager.active_ability

    def is_active(self, pos):
        for element in self.ui.elements.itervalues():
            if element.parent is None and element.point_is_over(pos):
                return False
        return True

    def click(self, pos):

        # get battle map coord at mouse pos
        # if ability is valid for this pos, trigger ability

        ability = self.active_ability
        if self.ready and ability is not None:

            coord = self.get_battle_map_coord(pos)
            if ability.ability_valid_at_point(coord):
                ability.cast_ability(coord)

    def get_battle_map_coord(self, (mx, my)):

        vpx, vpy = self.state.view_port.coord  # pix location of viewport top left
        rx = mx - vpx
        ry = my - vpy

        # tile coords relative to screen
        x = rx / SCALE_TILE_W
        y = ry / SCALE_TILE_H

        vx, vy = self.state.view.coord.int_position

        return x + vx, y + vy
