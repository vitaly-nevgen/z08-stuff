from unittest import TestCase

from lesson9.hometasks.solution import (
    Circle,
    Rectangle,
)


class TestTask1and2(TestCase):
    def test_circle(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.get_area(), 78.53, places=1)

    def test_rectangle(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.get_area(), 200)

    def test_comparison(self):
        circle = Circle(10)
        rectangle = Rectangle(25, 15)

        self.assertTrue(circle < rectangle)
        self.assertFalse(circle > rectangle)
        self.assertTrue(circle <= rectangle)
        self.assertFalse(circle >= rectangle)
