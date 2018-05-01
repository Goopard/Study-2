"""
This is a unittest test suite for the function square_of_triangle from module square_counter.
"""

import unittest
import sys

from square_counter import distance
from io_redirect import StdOutRedirector


class PositiveTests(unittest.TestCase):
    def test_same_dots(self):
        self.assertEqual(distance([1, 1], [1, 1]), 0.0)

    def test_different_dots1(self):
        self.assertEqual(distance([1, 1], [0, 0]), 1.4142135623730951)

    def test_different_dots2(self):
        self.assertEqual(distance([12.3, -54.178], [-45, 34.19]), 105.31948264210187)


class NegativeTests(unittest.TestCase):
    def test_too_many_coordinates_for_the_dot(self):
        with StdOutRedirector():
            self.assertEqual(distance([1, 2, 3, 4], [1, 1]), None)
            self.assertEqual(sys.stdout.getvalue(), 'ERROR: two lists of 2 elements expected, got 4, 2.\n')

    def test_wrong_type_of_arguments(self):
        with StdOutRedirector():
            self.assertEqual(distance([1, 1], 'a'), None)
            self.assertEqual(sys.stdout.getvalue(),
                             "ERROR: two lists of floats expected as arguments, got <class 'list'>, <class 'str'>.\n")

    def test_wrong_type_of_coordinates(self):
        with StdOutRedirector():
            self.assertEqual(distance([1, 'a'], [0, 0]), None)
            self.assertEqual(sys.stdout.getvalue(), "ERROR: type int or float expected, got <class 'str'>.\n")

    def test_too_few_arguments(self):
        with StdOutRedirector():
            self.assertEqual(distance(), None)
            self.assertEqual(sys.stdout.getvalue(), "ERROR: two arguments expected, got 0.\n")

    def test_too_many_arguments(self):
        with StdOutRedirector():
            self.assertEqual(distance([1, 1], [1, 1], [1, 1]), None)
            self.assertEqual(sys.stdout.getvalue(), "ERROR: two arguments expected, got 3.\n")


if __name__ == '__main__':
    unittest.main()