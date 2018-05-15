"""
This is unittest test suite for the function make_columns from the module stats.base.
"""

import unittest
from stats.base import make_columns


class PositiveTests(unittest.TestCase):
    """
    These are positive tests for the function make_columns from the module stats.base.
    """
    def test_two_rows_of_two(self):
        """
        This test checks if function deals correctly with the argument [['a', 'b'], [1, 2], [3, 4]].
        """
        self.assertEqual(make_columns([['a', 'b'], [1, 2], [3, 4]]), {'a': [1, 3], 'b': [2, 4]})

    def test_three_rows_of_three(self):
        """
        This test checks if function deals correctly with the argument [['a', 'b', 'c'], [1, 2, 3], [4, 5, 6],
        [7, 8, 9]].
        """
        self.assertEqual(make_columns([['a', 'b', 'c'], [1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                         {'a': [1, 4, 7], 'b': [2, 5, 8], 'c': [3, 6, 9]})

    def test_empty_data_list(self):
        """
        This tests checks if function deals correctly with the argument [].
        """
        self.assertEqual(make_columns([]), {})


class NegativeTests(unittest.TestCase):
    """
    These are negative tests for the function make_columns from the module stats.base.
    """

    def test_str(self):
        """
        This test checks if function deals correctly with the argument [['a', 'b'], [1]].
        """
        with self.assertRaises(ValueError) as error:
            make_columns([['a', 'b'], [1]])
        self.assertEqual(error.exception.args[0], 'rows in data_list must have equal lengths')
