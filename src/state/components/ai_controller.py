from state_component import StateComponent


class AIController(StateComponent):

    def __init__(self, state):

        StateComponent.__init__(self, state)

    @property
    def object_manager(self):
        return self.state.level.object_manager

    def run(self):

        if self.state.turn_tracker.is_monster_turn:

            self.run_neutral_objects()
            self.run_monsters()

    def run_neutral_objects(self):

        objects = self.object_manager.get_all('NEUTRAL')

        map(lambda x: x.spend_turn(), objects)

    def run_monsters(self):

        monsters = self.object_manager.get_all('AI')

        monsters = sorted(monsters, key=self.distance_to_player)

        map(lambda x: x.take_turn(), monsters)

        self.state.turn_tracker.end_monster_turn()

    def distance_to_player(self, obj):

        mx, my = obj.coord.int_position
        px, py = self.state.player.coord.int_position

        return abs(mx - px) + abs(my - py)

