from unittest import TestCase

from lesson9.hometasks.solution import (
    Circle,
    Triangle,
    FiguresRegistry,
)


class TestTask3(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.circle1 = Circle(8)
        cls.circle2 = Circle(10)
        cls.triangle = Triangle(10, 15, 10)

    def test_from_registry(self):
        self.assertEqual(
            FiguresRegistry().get_list(Circle),
            [self.circle1, self.circle2]
        )

        self.assertEqual(
            FiguresRegistry().get_list(Triangle),
            [self.triangle]
        )

    def test_from_class(self):
        self.assertEqual(
            Circle.get_list(),
            [self.circle1, self.circle2]
        )

        self.assertEqual(
            Triangle.get_list(),
            [self.triangle]
        )

    def test_triangle(self):
        self.assertAlmostEqual(
            self.triangle.get_area(), 49.60, places=1
        )