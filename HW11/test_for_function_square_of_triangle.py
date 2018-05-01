"""
This is a unittest test suite for the function square_of_triangle from module square_counter.
"""

import unittest
import sys

from square_counter import square_of_triangle
from io_redirect import StdOutRedirector


class PositiveTests(unittest.TestCase):
    """
    This test case contents the positive tests for the function square_of_triangle from the module square_counter.
    """
    def test_degenerate_triangle_1(self):
        """
        This test checks if the function square_of_triangle correctly counts the square of the degenerate triangle with
        vertexes (1, 1), (1, 1), (1, 1).
        """
        self.assertEqual(square_of_triangle([1, 1, 1, 1, 1, 1]), 0.0)

    def test_degenerate_triangle_2(self):
        """
        This test checks if the function square_of_triangle correctly counts the square of the degenerate triangle with
        vertexes (1, 1), (0, 0), (-1, -1).
        """
        self.assertEqual(square_of_triangle([1, 1, 0, 0, -1, -1]), 0.0)

    def test_not_degenerate_triangle_1(self):
        """
        This test checks if the function square_of_triangle correctly counts the square of the triangle with vertexes
        (1, 1), (0, 0), (1, 0).
        """
        self.assertAlmostEqual(square_of_triangle([1, 1, 0, 0, 1, 0]), 0.5, delta=0.00001)

    def test_not_degenerate_triangle_2(self):
        """
        This test checks if the function square_of_triangle correctly counts the square of the triangle with vertexes
        (1, 1), (-1, -1), (1, -1).
        """
        self.assertAlmostEqual(square_of_triangle([1, 1, -1, -1, 1, -1]), 2, delta=0.00001)


class NegativeTests(unittest.TestCase):
    """
    This test case contents the negative tests for the function square_of_triangle from the module square_counter.
    """
    def test_two_coordinates(self):
        """
        This test checks if the function square_counter correctly deals with the incorrect input data - too short
        coordinate list.
        """
        with StdOutRedirector():
            self.assertEqual(square_of_triangle([0, 0]), None)
            self.assertEqual(sys.stdout.getvalue(), 'ERROR: 6 coordinates expected, got 2.\n')

    def test_ten_coordinates(self):
        """
        This test checks if the function square_counter correctly deals with the incorrect input data - too long
        coordinate list.
        """
        with StdOutRedirector():
            self.assertEqual(square_of_triangle([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), None)
            self.assertEqual(sys.stdout.getvalue(), 'ERROR: 6 coordinates expected, got 10.\n')

    def test_wrong_coordinate_type(self):
        """
        This test checks if the function square_counter correctly deals with the incorrect input data - wrong types of
        the coordinates.
        """
        with StdOutRedirector():
            self.assertEqual(square_of_triangle([0, 0, 1, 2, 0, 'a']), None)
            self.assertEqual(sys.stdout.getvalue(), "ERROR: type int or float expected, got <class 'str'>.\n")

    def test_wrong_argument_for_the_function(self):
        """
        This test checks if the function square_counter correctly deals with the incorrect input data - wrong type of
        the argument (not list).
        """
        with StdOutRedirector():
            self.assertEqual(square_of_triangle('a'), None)
            self.assertEqual(sys.stdout.getvalue(),
                             "ERROR: list of vertexes expected as an argument, got <class 'str'>.\n")

    def test_too_few_arguments_for_the_function(self):
        """
        This test checks if the function square_counter correctly deals with the incorrect input data - too few
        arguments.
        """
        with StdOutRedirector():
            self.assertEqual(square_of_triangle(), None)
            self.assertEqual(sys.stdout.getvalue(),
                             "ERROR: one argument expected, got 0.\n")

    def test_too_many_arguments_for_the_function(self):
        """
        This test checks if the function square_counter correctly deals with the incorrect input data - too many
        arguments.
        """
        with StdOutRedirector():
            self.assertEqual(square_of_triangle([1, 2, 3, 4, 5, 6], 'afdfafadfa'), None)
            self.assertEqual(sys.stdout.getvalue(),
                             "ERROR: one argument expected, got 2.\n")


if __name__ == '__main__':
    unittest.main()
