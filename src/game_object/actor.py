from game_object import GameObject
from components.image_component import ImageComponent


class Actor(GameObject):

    def __init__(self, level_map, coord, image_id):

        GameObject.__init__(self, level_map, coord)
        self.image_component = ImageComponent(self, image_id)
        self.position(self.coord.position)

    def move(self, vector):
        self.coord.add(vector)
        self.position(self.coord.position)
