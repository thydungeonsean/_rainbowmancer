

class GameObjectComponent(object):

    def __init__(self, owner):

        self.owner = owner

    @property
    def game_state(self):
        return self.owner.game_state
