from tile_image import TileImage


class ImageCache(object):

    cache = {}

    @classmethod
    def get_tile_image(cls, tile_id):
        if tile_id not in cls.cache:
            cls.cache[tile_id] = TileImage(tile_id)

        return cls.cache[tile_id]
