"""
This is a unittest test suite for the function square_of_triangle from module square_counter.
"""

import unittest
import sys

from area_counter import distance
from io_redirect import StdOutRedirector


class PositiveTests(unittest.TestCase):
    """
    This test case contains positive tests for the function distance from the module area_counter.
    """
    def test_same_dots(self):
        """
        This test checks if function works correctly for the dots [1, 1] and [1, 1].
        """
        self.assertEqual(distance([1, 1], [1, 1]), 0.0)

    def test_different_dots1(self):
        """
        This test check if function works correctly for the dots [1, 1] and [0, 0].
        """
        self.assertEqual(distance([1, 1], [0, 0]), 1.4142135623730951)

    def test_different_dots2(self):
        """
        This test check if function works correctly for the dots [12.3, -54.178] and [-45, 34.19].
        """
        self.assertEqual(distance([12.3, -54.178], [-45, 34.19]), 105.31948264210187)


class NegativeTests(unittest.TestCase):
    """
    This test case contains the negative tests for the function distance from module area_counter.
    """
    def test_too_many_coordinates_for_the_dot(self):
        """
        This test checks if function correctly deals with the incorrect input data - too many coordinates for the first
        dot.
        """
        with StdOutRedirector():
            self.assertEqual(distance([1, 2, 3, 4], [1, 1]), None)
            self.assertEqual(sys.stdout.getvalue(), 'ERROR: two lists of 2 elements expected, got 4, 2.\n')

    def test_wrong_type_of_arguments(self):
        """
        This test checks if function correctly deals with the incorrect input data - wrong type of the argument.
        """
        with StdOutRedirector():
            self.assertEqual(distance([1, 1], 'a'), None)
            self.assertEqual(sys.stdout.getvalue(),
                             "ERROR: two lists of floats expected as arguments, got <class 'list'>, <class 'str'>.\n")

    def test_wrong_type_of_coordinates(self):
        """
        This test checks if function correctly deals with the incorrect input data - wrong type of the coordinates.
        """
        with StdOutRedirector():
            self.assertEqual(distance([1, 'a'], [0, 0]), None)
            self.assertEqual(sys.stdout.getvalue(), "ERROR: type int or float expected, got <class 'str'>.\n")

    def test_too_few_arguments(self):
        """
        This test checks if function correctly deals with the incorrect input data - too few arguments.
        """
        with StdOutRedirector():
            self.assertEqual(distance(), None)
            self.assertEqual(sys.stdout.getvalue(), "ERROR: two arguments expected, got 0.\n")

    def test_too_many_arguments(self):
        """
        This test checks if function correctly deals with the incorrect input data - too many arguments.
        """
        with StdOutRedirector():
            self.assertEqual(distance([1, 1], [1, 1], [1, 1]), None)
            self.assertEqual(sys.stdout.getvalue(), "ERROR: two arguments expected, got 3.\n")


if __name__ == '__main__':
    unittest.main()