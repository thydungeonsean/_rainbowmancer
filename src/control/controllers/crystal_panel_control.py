from panel_control import PanelControl
from src.control.ui.layout_constants import *
from src.enum.hues import *
from src.map.color_components.spot_source import SpotColorSource


class CrystalPanelControl(PanelControl):

    crystal_hue = {
        'red_crystal': RED_HUE,
        'green_crystal': GREEN_HUE,
        'blue_crystal': BLUE_HUE,
        'yellow_crystal': YELLOW_HUE,
        'purple_crystal': PURPLE_HUE,
        'cyan_crystal': CYAN_HUE,
    }

    primary_hues = {RED_HUE, GREEN_HUE, BLUE_HUE}

    def __init__(self, ui):

        self.crystal_map = {}
        self.crystal_sources = {}
        PanelControl.__init__(self, ui)

    @property
    def player(self):
        return self.state.player

    @property
    def color_map(self):
        return self.player.level_map.color_map

    @property
    def pos(self):
        return self.player.coord.int_position

    def load_buttons(self):

        for crystal, i in crystal_sequence:

            crystal_id = '_'.join((crystal, 'crystal'))
            element = self.ui.get_element(crystal_id)
            self.buttons.append(element)
            element.on_click = self.create_click_function(crystal_id)
            element.button_component.deactivate()
            self.crystal_map[crystal_id] = False

    def click(self, key):
        if self.taking_input:

            element = self.ui.get_element(key)
            if element.button_component.active:
                if not self.crystal_map[key]:

                    self.select_crystal(key)

                else:

                    self.deselect_crystal(key)

    def select_crystal(self, crystal_id):

        self.crystal_map[crystal_id] = True

        element = self.ui.get_element(crystal_id).button_component
        element.focus_on()
        element.start_glowing()
        # TODO - highlight crystal cost
        self.set_color_source(crystal_id)
        self.request_update()

    def deselect_crystal(self, crystal_id):

        self.crystal_map[crystal_id] = False

        element = self.ui.get_element(crystal_id).button_component
        element.focus_off()
        element.stop_glowing()
        # TODO - clear crystal cost
        self.clear_color_source(crystal_id)
        self.request_update()

    def deselect_all(self):

        for button in self.buttons:
            self.deselect_crystal(button.element_id)

    def update(self):
        self.update_buttons()
        self.ui.ability_controller.update_button_color()

    def update_buttons(self):

        player_hue = self.player.color_component.current_hue
        for button in self.buttons:

            if self.button_is_active(button, player_hue):
                button.button_component.activate()

            elif self.crystal_map[button.element_id]:
                # if button is selected already, then it stays active
                button.button_component.activate()

            else:
                button.button_component.deactivate()

    def button_is_active(self, button, player_hue):

        sufficient_crystals = True
        valid_hue = self.hue_is_valid(button, player_hue)
        return sufficient_crystals and valid_hue

    def hue_is_valid(self, button, player_hue):

        button_hue = CrystalPanelControl.crystal_hue[button.element_id]

        if player_hue == WHITE_HUE and self.color_map.get_tile(self.pos) == DARK_HUE:
            return True
        return player_hue in CrystalPanelControl.primary_hues and button_hue in CrystalPanelControl.primary_hues and \
            player_hue != button_hue

    def set_color_source(self, crystal_id):

        hue = CrystalPanelControl.crystal_hue[crystal_id]

        source = SpotColorSource(self.color_map, hue, self.pos)
        self.crystal_sources[crystal_id] = source

    def clear_color_source(self, crystal_id):

        if crystal_id in self.crystal_sources:
            source = self.crystal_sources[crystal_id]
            source.kill()
            del self.crystal_sources[crystal_id]

    def reset_crystals(self, free):

        if free:
            pass
        else:
            pass

        self.deselect_all()
