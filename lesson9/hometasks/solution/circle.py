import math
from lesson9.hometasks.solution import Figure

__all__ = (
    'Circle'
)


class Circle(Figure):
    r = None

    def __init__(self, r):
        self.r = r
        super().__init__()

    def get_area(self):
        return math.pi * (self.r**2)

    def __repr__(self):
        return 'Circle(r={})'.format(self.r)
