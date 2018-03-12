from game_object_component import GameObjectComponent


class TurnComponent(GameObjectComponent):

    READY = 0
    USED = 1
    STUNNED = 2

    def __init__(self, owner):

        GameObjectComponent.__init__(self, owner)
        self.state = TurnComponent.READY

    def take_turn(self):

        self.state = TurnComponent.USED

    def refresh_turn(self):

        self.state = TurnComponent.READY

    @property
    def ready(self):
        return self.state == TurnComponent.READY

