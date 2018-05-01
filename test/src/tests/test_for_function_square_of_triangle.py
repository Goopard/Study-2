"""
This is a unittest test suite for the module square_counter.
"""

import unittest
import sys
import io

from ..triangle.square_counter import square_of_triangle


class StdOutRedirector:
    """
    This class is used to temporary redirect the output of the code into a StringIO object.
    """
    def __enter__(self):
        self.old_stdout = sys.stdout
        sys.stdout = io.StringIO()

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.old_stdout


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
            self.assertEqual(sys.stdout.getvalue(), 'ERROR: 6 coordinates expected, got 2\n')

    def test_ten_coordinates(self):
        """
        This test checks if the function square_counter correctly deals with the incorrect input data - too long
        coordinate list.
        """
        with StdOutRedirector():
            self.assertEqual(square_of_triangle([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), None)
            self.assertEqual(sys.stdout.getvalue(), 'ERROR: 6 coordinates expected, got 10\n')

    def test_wrong_coordinate_type(self):
        """
        This test checks if the function square_counter correctly deals with the incorrect input data - wrong types of
        the coordinates.
        """
        with StdOutRedirector():
            self.assertEqual(square_of_triangle([0, 0, 1, 2, 0, 'a']), None)
            self.assertEqual(sys.stdout.getvalue(), "ERROR: type int or float expected, got <class 'str'>\n")

    def test_wrong_argument_for_the_function(self):
        """
        This test checks if the function square_counter correctly deals with the incorrect input data - wrong type of
        the argument (not list).
        """
        with StdOutRedirector():
            self.assertEqual(square_of_triangle('a'), None)
            self.assertEqual(sys.stdout.getvalue(),
                             "ERROR: list of vertexes expected as an argument, got <class 'str'>\n")


if __name__ == '__main__':
    unittest.main()
