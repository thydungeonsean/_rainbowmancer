from state_component import StateComponent
from src.abilities.ability_archive import AbilityArchive


class AbilityManager(StateComponent):

    def __init__(self, state):

        StateComponent.__init__(self, state)

        self.active_ability = None
        self.panel_control = None
        self.archive = None

    def set_panel_control(self, panel):
        self.panel_control = panel
        self.archive = AbilityArchive(self)

    def update_panel_color(self):
        self.panel_control.update_button_color()

    def ability_can_be_cast(self, ability_key):

        ability = self.archive.get_ability(ability_key)
        return ability.can_be_cast()

    def select_ability(self, ability_key):
        self.active_ability = self.archive.get_ability(ability_key)
        self.active_ability.set_active()

    def deselect_ability(self):
        if self.active_ability is not None:
            self.active_ability.reset()
        self.active_ability = None
