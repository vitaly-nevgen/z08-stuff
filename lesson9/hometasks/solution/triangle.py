import math
from lesson9.hometasks.solution import Figure

__all__ = (
    'Triangle'
)


class Triangle(Figure):
    a = None
    b = None
    c = None

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()

    def get_area(self):
        p = (self.a + self.b + self.c) / 2.
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def __repr__(self):
        return 'Triangle(a={}, b={}, c={})'.format(self.a, self.b, self.c)
