

class ObjectManager(object):

    def __init__(self, level):

        self.level = level
        self.game_state = self.level.game_state

        self.objects = []

    def draw(self, surface):

        for obj in self.objects:

            if self.object_in_viewport(obj):
                obj.draw(surface)

    def object_in_viewport(self, obj):

        return self.game_state.view.coord_in_view(obj.coord)

    def add_object(self, obj):

        obj.set_position()
        self.objects.append(obj)

