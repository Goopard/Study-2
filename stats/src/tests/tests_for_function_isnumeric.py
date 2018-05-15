"""
This is unittest test suite for the function isnumeric from the module stats.base.
"""

import unittest
from stats.base import isnumeric


class PositiveTests(unittest.TestCase):
    """
    These are positive tests for the function isnumeric from the module stats.base.
    """
    def test_float(self):
        """
        This test checks if function deals correctly with the argument 1.9.
        """
        self.assertTrue(isnumeric(1.9))

    def test_int(self):
        """
        This test checks if function deals correctly with the argument 1.
        """
        self.assertTrue(isnumeric(1))

    def test_list_int(self):
        """
        This test checks if function deals correctly with the argument [1, 2, 3].
        """
        self.assertTrue(isnumeric([1, 2, 3]))


class NegativeTests(unittest.TestCase):
    """
    These are negative tests for the function isnumeric from the module stats.base.
    """

    def test_str(self):
        """
        This test checks if function deals correctly with the argument 'a'.
        """
        self.assertFalse(isnumeric('a'))

    def test_list_with_str(self):
        """
        This test checks if function deals correctly with the argument [1, 2, 'a'].
        """
        self.assertFalse(isnumeric([1, 2, 'a']))
