from panel_control import PanelControl
from src.enum.abilities import *
from src.enum.hues import *


class AbilityPanelControl(PanelControl):

    def __init__(self, ui):

        self.ability_map = {}
        self.ability_color = WHITE_HUE
        PanelControl.__init__(self, ui)
        self.ability_manager.set_panel_control(self)

    @property
    def ability_manager(self):
        return self.state.ability_manager

    @property
    def player(self):
        return self.state.player

    def load_buttons(self):

        for ability_id in ability_id_to_string.itervalues():
            element = self.ui.get_element(ability_id)
            self.buttons.append(element)
            element.on_click = self.create_click_function(ability_id)

            self.ability_map[ability_id] = False

    def update(self):

        self.update_buttons()

    def update_buttons(self):

        # TODO check which buttons can be clicked, deactivate all others
        # for each button
        # 1 is it active
        # 2 is it selected

        for button in self.buttons:

            if self.ability_can_be_cast(button.element_id):
                button.button_component.activate()
            else:
                button.button_component.deactivate()

            if self.ability_map[button.element_id]:
                button.button_component.start_glowing()
                button.button_component.focus_on()
            else:
                button.button_component.stop_glowing()
                button.button_component.focus_off()

    def update_button_color(self):

        hue_id = self.get_player_hue()

        # TODO can modify this color with crystal buttons

        self.ability_color = hue_id

        for button in self.buttons:
            button.button_component.change_color(hue_id)

        self.request_update()

    def get_player_hue(self):

        return self.player.color_component.current_hue

    def click(self, key):
        if self.taking_input:

            if self.ability_map[key]:

                self.deselect_ability(key)

            elif not self.ability_map[key] and self.ability_can_be_cast(key):

                self.deselect_all()
                self.select_ability(key)

    def ability_can_be_cast(self, key):
        return self.ability_manager.ability_can_be_cast(key)

    def deselect_all(self):
        for key in self.ability_map.keys():
            self.deselect_ability(key)

    def select_ability(self, key):
        self.ability_map[key] = True
        self.request_update()

        self.ability_manager.select_ability(key)

    def deselect_ability(self, key):
        self.ability_map[key] = False
        self.request_update()

        self.ability_manager.deselect_ability()
