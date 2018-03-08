

class RedrawManager(object):

    def __init__(self, level):

        self.level = level
        self.redraw_tile_set = set()

    def set_redraw_tiles(self, fov):
        self.redraw_tile_set.update(fov)

    def run(self):

        if self.level.color_map.needs_recompute:

            self.level.color_map.recompute_color_map()
            redrawn_tiles = self.level.color_map.get_differing_tiles()
            self.redraw_tile_set.update(redrawn_tiles)

            # update color components of any changed tiles
            self.update_color_components(redrawn_tiles)

        if self.redraw_tile_set:

            self.level.map_image.redraw_tiles(self.redraw_tile_set)
            self.redraw_tile_set.clear()

    def update_color_components(self, changed_tiles):

        for tile in changed_tiles:
            # TODO if object manager says there is a reflector component or generator component there, update it
            # self.level.object_manager
            pass
