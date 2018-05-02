"""
This is a unittest test suite for the function read_triangle from the module area_counter.
"""

import unittest

from area_counter import read_triangle
from io_redirect import StdInRedirector, StdOutRedirector


class Tests(unittest.TestCase):
    """
    This test case contents the tests for the function read_triangle from module area_counter.
    """
    def test_entered_from_the_first_try(self):
        """
        This test checks if the function read_triangle works correctly with some correct input.
        """
        with StdInRedirector('1 2\n1 2\n1 2\n'), StdOutRedirector():
            self.assertEqual(read_triangle(), [1.0, 2.0, 1.0, 2.0, 1.0, 2.0])

    def test_entered_from_the_second_try_because_of_too_many_coordinates(self):
        """
        This test checks if the function read_triangle works correctly assuming that user entered to many coordinates
        for the first vertex.
        """
        with StdInRedirector('1 2 3\n1 2\n1 2\n1 2\n'), StdOutRedirector():
            self.assertEqual(read_triangle(), [1.0, 2.0, 1.0, 2.0, 1.0, 2.0])

    def test_entered_from_the_second_try_because_of_wrong_type(self):
        """
        This test checks if the function read_triangle works correctly assuming that user entered coordinates with the
        wrong type for the first vertex.
        """
        with StdInRedirector('1 a\n1 2\n1 2\n1 2\n'), StdOutRedirector():
            self.assertEqual(read_triangle(), [1.0, 2.0, 1.0, 2.0, 1.0, 2.0])

    def test_entered_from_the_second_try_because_of_too_few_coordinates(self):
        """
        This test checks if the function read_triangle works correctly assuming that user entered to few coordinates
        for the first vertex.
        """
        with StdInRedirector('\n1 2\n1 2\n1 2\n'), StdOutRedirector():
            self.assertEqual(read_triangle(), [1.0, 2.0, 1.0, 2.0, 1.0, 2.0])


if __name__ == '__main__':
    unittest.main()
