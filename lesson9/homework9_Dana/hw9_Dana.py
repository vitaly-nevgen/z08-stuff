import math


class Figure:

    def get_area(self):
        pass

    def __add__(self, other):
        return self.get_area() + other

    def __radd__(self, other):
        return self.get_area() + other

    def __lt__(self, other):
        return self.get_area() < other

    def __eq__(self, other):
        return self.get_area() == other

    def __ge__(self, other):
        return self.get_area() >= other


class Circle(Figure):
    radius = None

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        circle_area = round(math.pi * self.radius ** 2, 3)
        return circle_area

    def __str__(self):
        return 'Circle with radius \'{}\''.format(self.radius)


class Rectangle(Figure):
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Rectangle with sides \'{}\' and \'{}\''.format(self.a, self.b)

    def get_area(self):
        rectangle_area = self.a * self.b
        return rectangle_area


class Triangle(Figure):
    a = None
    b = None
    c = None

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return 'Triangle with sides \'{}\' , \'{}\' and \'{}\''.format(self.a, self.b, self.c)

    def get_area(self):
        p = (self.a + self.b + self.c)/2
        triangle_area = round(math.sqrt(p * (p - self.a) * (p - self.b) *(p - self.c)), 3)
        return triangle_area


rad = 5

r_side1 = 8
r_side2 = 3

t_side1 = 3
t_side2 = 5
t_side3 = 4


circle = Circle(rad)
print('{} has area of: '.format(str(circle)), circle.get_area())

rectangle = Rectangle(r_side1, r_side2)
print('{} has area of: '.format(str(rectangle)), rectangle.get_area())

triangle = Triangle(t_side1, t_side2, t_side3)
print('{} has area of: '.format(str(triangle)), triangle.get_area())
