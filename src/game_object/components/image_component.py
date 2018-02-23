from game_object_component import GameObjectComponent
from src.data_structures.vector import Vector
from src.image.tile_image import TileImage


class ImageComponent(GameObjectComponent):

    A = 0
    B = 1

    def __init__(self, owner, image_id):

        GameObjectComponent.__init__(self, owner)
        self.image_id = image_id
        self.images = self.load_images()

    @property
    def frame(self):
        return self.game_state.frame

    @property
    def color_id(self):
        return self.images[0].color_id

    def load_images(self):

        images = {
            ImageComponent.A: TileImage(self.image_id),
            ImageComponent.B: TileImage(self.image_id, animated_frame=True)
        }

        return images

    def position(self, (x, y)):

        for i in (0, 1):
            self.images[i].position((x, y))

    def draw(self, surface):

        image = self.images[self.frame]
        image.draw(surface)

    def change_color(self, new_color):

        if new_color != self.color_id:
            for i in (0, 1):
                self.images[i].change_color(new_color)

    @property
    def w(self):
        return self.images[0].w

    @property
    def h(self):
        return self.images[0].h
