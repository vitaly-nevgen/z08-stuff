import math


class Figure:

    def get_area(self):
        pass

    def __add__(self, other):
        return self.get_area() + other

    def __radd__(self, other):
        return self.get_area() + other

    def __lt__(self, other): #x<y calls x.__lt__(y)
        return self.get_area() < other

    def __gt__(self, other): #x>y calls x.__gt__(y)
        return self.get_area() > other

    def __le__(self, other): #x<=y calls x.__le__(y)
        return self.get_area() <= other

    def __eq__(self, other): #x==y calls x.__eq__(y)
        return self.get_area() == other

    def __ne__(self, other): #x!=y calls x.__ne__(y)
        return self.get_area() != other

    def __ge__(self, other): #x>=y calls x.__ge__(y)
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
        rect_area = self.a * self.b
        return rect_area


class Triangle(Figure):
    a = None
    b = None
    c = None

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = (self.a + self.b + self.c)/2
        triangle_area = round(math.sqrt(p * (p - self.a) * (p - self.b) *(p - self.c)), 3)
        return triangle_area


side1 = 2
side2 = 6
rad = 1
t_side1 = 4
t_side2 = 5
t_side3 = 2


rect1 = Rectangle(side1, side2)
print('{} has area: '.format(str(rect1)), rect1.get_area())

circle1 = Circle(rad)
print('{} has area: '.format(str(circle1)), circle1.get_area())

triangle1 = Triangle(t_side1, t_side2, t_side3)
print(triangle1.get_area())

if circle1 > rect1:
    print('Circle has greater area than rectangle')
else:
    print('Rectangle has greater area than circle')
