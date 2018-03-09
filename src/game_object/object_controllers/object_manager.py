

class ObjectManager(object):

    def __init__(self, level):

        self.level = level
        self.game_state = self.level.game_state

        self.objects = []

    def run(self):
        for obj in self.objects:
            obj.run()

    def draw(self, surface):

        for obj in self.objects:

            if self.object_in_viewport(obj) and self.object_is_visible(obj):
                obj.draw(surface)

    def object_in_viewport(self, obj):

        return self.game_state.view.coord_in_view(obj.coord)

    def object_is_visible(self, obj):
        point = obj.coord.int_position
        return point in self.game_state.level.fov_map.visible

    def add_object(self, obj):

        obj.set_position()
        self.objects.append(obj)
        self.level.fov_map.update_point(obj.coord.int_position)

    def point_is_obstructed(self, point):

        objects = self.get_objects_at_point(point)
        if objects:
            for obj in objects:
                if obj.blocks_sight:
                    return True
        return False

    def point_is_blocked(self, point):

        objects = self.get_objects_at_point(point)
        if objects:
            for obj in objects:
                if obj.blocks:
                    return True
        return False

    def update_positions(self):
        for obj in self.objects:
            obj.set_position()

    def get_objects_at_point(self, point):

        return filter(lambda x: x.coord.position == point, self.objects)
