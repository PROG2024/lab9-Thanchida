"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
import math


class CircleTest(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(3)
        self.check = ''

    def test_two_circle_have_positive_radius(self):
        self.assertEqual(self.circle.get_radius(), 3)
        radius = self.circle.get_radius()
        self.assertEqual(self.circle.get_area(), math.pi*radius*radius)

        second_circle = Circle(4)
        result = self.circle.add_area(second_circle)
        self.assertEqual(result.get_radius(), 5)

    def test_result_should_have_same_radius(self):
        second_circle = Circle(0)
        result = self.circle.add_area(second_circle)
        self.assertEqual(result.get_radius(), self.circle.get_radius())

    def test_radius_is_not_negative(self):
        with self.assertRaises(ValueError):
            self.check = Circle(-5)

