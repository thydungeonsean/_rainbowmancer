from ui import UI
from element import Element
from layout_constants import *
from components.border_component import BorderComponent
from components.icon_component import IconComponent
from src.enum.ui import *
from src.control.controllers.ability_panel_control import AbilityPanelControl
from src.control.controllers.crystal_panel_control import CrystalPanelControl


class Layout(object):

    instance = None

    @classmethod
    def get_instance(cls):

        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    @classmethod
    def create_game_ui(cls, state):

        ui = UI(state)

        layout = cls.get_instance()
        layout.create_side_panel(ui)
        layout.create_ability_panel(ui)
        layout.create_crystal_panel(ui)
        layout.create_player_panel(ui)

        ui.add_controller(AbilityPanelControl(ui))
        ui.add_controller(CrystalPanelControl(ui))

        return ui

    def __init__(self):
        pass

    def create_element(self, ui, w, h, coord=(0, 0), parent=None, el_id=None):

        ui.add_element(Element(ui, w, h, coord=coord, parent=parent, el_id=el_id))

    def create_side_panel(self, ui):

        w = side_panel_w
        h = side_panel_h
        coord = side_panel_coord
        el_id = 'side_panel'

        self.create_element(ui, w, h, coord=coord, el_id=el_id)

    def create_ability_panel(self, ui):

        w = ability_panel_w
        h = ability_panel_h
        coord = ability_panel_coord
        parent = 'side_panel'
        el_id = 'ability_panel'

        self.create_element(ui, w, h, coord=coord, parent=parent, el_id=el_id)

        self.add_border_component(ui, el_id)
        self.add_ability_icons(ui)

    def create_crystal_panel(self, ui):

        w = crystal_panel_w
        h = crystal_panel_h
        parent = 'side_panel'
        el_id = 'crystal_panel'

        self.create_element(ui, w, h, parent=parent, el_id=el_id)

        self.add_border_component(ui, el_id)
        self.add_crystal_icons(ui)

    def create_player_panel(self, ui):

        w = player_panel_w
        h = player_panel_h
        coord = player_panel_coord
        parent = 'side_panel'
        el_id = 'player_panel'

        self.create_element(ui, w, h, coord=coord, parent=parent, el_id=el_id)

        self.add_border_component(ui, el_id)

    def add_border_component(self, ui, key):

        element = ui.get_element(key)
        element.add_component(BorderComponent(element, style=1))

    def add_crystal_icons(self, ui):

        for c in range(6):
            self.add_crystal_icon(ui, c)

    def add_crystal_icon(self, ui, c):

        w = ICON_W
        h = ICON_H
        coord = TILE_W, TILE_H + c * ICON_H
        parent = 'crystal_panel'
        el_id = crystal_sequence[c][0] + '_crystal'

        self.create_element(ui, w, h, coord=coord, parent=parent, el_id=el_id)

        self.add_icon_component(ui, el_id, CRYSTAL_ICON, crystal_sequence[c][1])

    def add_icon_component(self, ui, el_id, icon_id, hue_id):

        element = ui.get_element(el_id)
        icon =IconComponent(element, icon_id, hue_id)
        # icon.focus_on()
        element.add_component_as_button(icon)

    def add_ability_icons(self, ui):

        # TODO get available abilities from player object

        abilities = ability_sequence

        for i in range(len(abilities)):
            self.create_ability_icon(ui, abilities, i)

    def create_ability_icon(self, ui, abilities, i):

        w = ICON_W
        h = ICON_H
        coord = TILE_W, TILE_H + i * ICON_H
        parent = 'ability_panel'
        el_id = abilities[i][0]
        icon_id = abilities[i][1]

        self.create_element(ui, w, h, coord=coord, parent=parent, el_id=el_id)
        self.add_ability_component(ui, el_id, icon_id)

    def add_ability_component(self, ui, el_id, icon_id):

        element = ui.get_element(el_id)
        element.add_component_as_button(IconComponent(element, icon_id, WHITE_HUE))
