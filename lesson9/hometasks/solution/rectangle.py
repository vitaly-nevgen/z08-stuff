from lesson9.hometasks.solution import Figure

__all__ = (
    'Rectangle'
)


class Rectangle(Figure):
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()

    def get_area(self):
        return self.a * self.b

    def __repr__(self):
        return 'Rectangle(a={}, b={})'.format(self.a, self.b)
