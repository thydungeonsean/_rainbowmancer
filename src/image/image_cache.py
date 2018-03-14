from tile_image import TileImage
from ui_tile_image import UITileImage
from icon_image import IconImage


class ImageCache(object):

    cache = {}

    @classmethod
    def get_tile_image(cls, tile_id):
        if tile_id not in cls.cache:
            cls.cache[tile_id] = TileImage(tile_id)

        return cls.cache[tile_id]

    @classmethod
    def get_ui_tile_image(cls, tile_id):

        if tile_id not in cls.cache:
            cls.cache[tile_id] = UITileImage(tile_id)

        return cls.cache[tile_id]

    @classmethod
    def get_icon_image(cls, tile_id):

        if tile_id not in cls.cache:
            cls.cache[tile_id] = IconImage(tile_id)

        return cls.cache[tile_id]
