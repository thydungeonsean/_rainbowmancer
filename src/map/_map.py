

class _Map(object):

    def __init__(self, w, h):

        self.map = [[self.start_value() for my in range(h)] for mx in range(w)]
        self.w = w
        self.h = h

    @staticmethod
    def start_value():
        return 0

    def get_tile(self, (x, y)):
        return self.map[x][y]

    def set_tile(self, (x, y), value):
        self.map[x][y] = value

    @property
    def all_points(self):

        for x, y in [(x, y) for y in range(self.h) for x in range(self.w)]:
            yield x, y

    def point_in_bounds(self, (x, y)):

        return 0 <= x < self.w and 0 <= y < self.h

    def get_adj(self, (x, y), diag=False):

        adj = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if diag:
            adj.extend([(x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)])
        return list(filter(self.point_in_bounds, adj))
