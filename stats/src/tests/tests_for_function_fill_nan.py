"""
This is unittest test suite for the function fill_nan from the module stats.base.
"""

import unittest
from stats.base import fill_nan


class Tests(unittest.TestCase):
    """
    These are tests for the function fill_nan from the module stats.base.
    """

    def test_list_of_ints(self):
        """
        This test checks if function deals correctly with the arguments [1, 2, NaN, 4], 3.
        """
        self.assertEqual(fill_nan([1, 2, float('NaN'), 4], 3), [1, 2, 3, 4])

    def test_list_of_floats(self):
        """
        This test checks if function deals correctly with the arguments [1.0, 2.0, NaN, 4.0, NaN], 3.0.
        """
        self.assertEqual(fill_nan([1.0, 2.0, float('NaN'), 4.0, float('NaN')], 3.0), [1.0, 2.0, 3.0, 4.0, 3.0])
