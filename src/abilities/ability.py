

class Ability(object):

    def __init__(self, manager):

        self.state = manager.state
        self.panel = manager.panel_control
        self.valid_points = set()

    @property
    def player(self):
        return self.state.player

    @property
    def object_manager(self):
        return self.state.level.object_manager

    @property
    def ability_hue(self):
        return self.state.player.color_component.current_hue

    @property
    def color_map(self):
        return self.state.level.color_map

    def set_active(self):
        self.compute_valid_points()

    def reset(self):
        self.valid_points.clear()

    def can_be_cast(self):
        sufficient_gems = True
        valid_target = True
        return sufficient_gems and valid_target

    def ability_valid_at_point(self, point):
        return point in self.valid_points

    def compute_valid_points(self):

        pass

    def cast_ability(self, coord):

        print 'zimpp'

    def get_visible(self):

        return self.state.level.fov_map.visible


