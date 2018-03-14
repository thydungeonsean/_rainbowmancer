

class Ability(object):

    def __init__(self, manager):

        self.state = manager.state
        self.panel = manager.panel_control
        self.valid_points = set()

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
