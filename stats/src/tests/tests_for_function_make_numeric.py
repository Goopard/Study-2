"""
This is unittest test suite for the function make_numeric from the module stats.base.
"""

import unittest
from stats.base import make_numeric


class PositiveTests(unittest.TestCase):
    """
    These are positive tests for the function make_numeric from the module stats.base.
    """
    def test_list_floats(self):
        """
        This test checks if function deals correctly with the argument ['1.2', '0.15', '-1.2'].
        """
        self.assertEqual(make_numeric(['1.2', '0.15', '-1.2']), [1.2, 0.15, -1.2])

    def test_list_ints(self):
        """
        This test checks if function deals correctly with the arguments ['1', '2', '3'], int.
        """
        self.assertEqual(make_numeric(['1', '2', '3'], int), [1, 2, 3])


class NegativeTests(unittest.TestCase):
    """
    These are negative tests for the function make_numeric from the module stats.base.
    """

    def test_list_ints_with_str(self):
        """
        This test checks if function deals correctly with the arguments ['1', '2', 'a'], int.
        """
        self.assertEqual(make_numeric(['1', '2', 'a'], int), ['1', '2', 'a'])

    def test_str(self):
        """
        This test checks if function deals correctly with the argument 'a'.
        """
        self.assertEqual(make_numeric('a'), 'a')

    def test_wrong_type(self):
        """
        This test checks if function deals correctly with the argument ['1', '2', '3'], str.
        """
        with self.assertRaises(ValueError) as error:
            make_numeric(['1', '2', '3'], str)
        self.assertEqual(error.exception.args[0],
                         "argument numeric_type can only have value <class 'int'> or <class 'float'>")

