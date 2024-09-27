from lesson9.hometasks.solution import FiguresRegistry

__all__ = (
    'Figure'
)


class Figure:
    def __init__(self):
        FiguresRegistry().add(self)

    def get_area(self):
        raise NotImplementedError

    @classmethod
    def get_list(cls):
        return FiguresRegistry().get_list(cls)

    def __lt__(self, other):
        return self.get_area() < other

    def __le__(self, other):
        return self.get_area() <= other

    def __gt__(self, other):
        return self.get_area() > other

    def __ge__(self, other):
        return self.get_area() >= other
