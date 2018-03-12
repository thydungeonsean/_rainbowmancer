from actor import Actor
from components.ai_component import AIComponent


class Enemy(Actor):

    def __init__(self, level_map, coord, actor_id):

        Actor.__init__(self, level_map, coord, actor_id)
        self.ai_component = self.load_ai_component()

    def load_ai_component(self):
        return AIComponent(self)

    def set_team(self):
        return 'AI'

    def on_bump(self, bumper):

        if bumper.team == "PLAYER":
            bumper.attack(self)
        else:
            bumper.spend_turn()

    def take_turn(self):

        self.ai_component.take_turn()
