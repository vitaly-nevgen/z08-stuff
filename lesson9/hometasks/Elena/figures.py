import math
import gc


class Figure:
    def get_area(self):
        pass

    def __init__(self):
        FiguresRegistry().add()

    def __lt__(self, figure):
        return self.get_area() < figure.get_area()

    def __le__(self, figure):
        return self.get_area() <= figure.get_area()

    def __eq__(self, figure):
        return self.get_area() == figure.get_area()

    def __ne__(self, figure):
        return self.get_area() != figure.get_area()

    def __gt__(self, figure):
        return self.get_area() > figure.get_area()

    def __ge__(self, figure):
        return self.get_area() >= figure.get_area()

    @classmethod
    def get_list(cls):
        objects_list = []
        for object in gc.get_objects():
            if isinstance(object, cls):
                objects_list.append(object)
        return objects_list


class Circle(Figure):
    radius = None

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * self.radius ** 2
        return round(area, 1)


class Rectangle(Figure):
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        area = self.a * self.b
        return area


class Triangle(Figure):
    a = None
    b = None
    c = None

    def __init__(self, a, b, c):
        if a + b > c and a + c > b and c + b > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            print('Triangle with specified sides is not existed')

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        area = math.sqrt(p(p - self.a) * (p - self.b) * (p - self.c))
        return area


class FiguresRegistry(object):
    _instance = None
    register = {}

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def add(cls):
        cls.register.update({cls.__class__: cls})
        return cls.register

    @classmethod
    def get_list(cls, instance):
        objects_list = []
        for object in gc.get_objects():
            if isinstance(object, instance):
                objects_list.append(object)
        return objects_list


if __name__ == '__main__':
    circle = Circle(5)
    rect = Rectangle(10, 20)

    if circle > rect:
        print('Circle has greater area than rectangle')
    else:
        print('Rectangle has greater area than circle')

    print(circle.get_area())  # returns 78.5
    print(rect.get_area())  # returns 200

    circle1 = Circle(5)
    circle2 = Circle(8)
    rect = Rectangle(10, 20)
    triangle = Triangle(5, 8, 10)

    print(FiguresRegistry().get_list(Circle))  # returns [<Circle>, <Circle>]
    print(FiguresRegistry().get_list(Rectangle))  # returns [<Rectangle>]
    print(FiguresRegistry().get_list(Triangle))  # returns [<Triangle>]
    print(Circle.get_list())