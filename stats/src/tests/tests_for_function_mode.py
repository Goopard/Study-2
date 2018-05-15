"""
This is a unittest test suite for the function mode from the module stats.stats.
"""
import unittest
from stats.stats import mode


class PositiveTests(unittest.TestCase):
    """
    This is positive test case for the function mode from the module stats.
    """
    def test_one_element(self):
        """
        This test checks if the function deals correctly with list of one element.
        """
        self.assertEqual(mode([1]), [1])

    def test_simple_int_list(self):
        """
        This test checks if the function deals correctly with list [1, 1, 1, 1, 1, 2, 3, 4, 5].
        """
        self.assertEqual(mode([1, 1, 1, 1, 1, 2, 3, 4, 5]), [1])

    def test_harder_int_list(self):
        """
        This test checks if the function deals correctly with list [1, 1, 2, 2, 1, 3, 5, 6, 7, 5].
        """
        self.assertEqual(mode([1, 1, 2, 2, 3, 5, 6, 7, 5]), [1, 2, 5])


class NegativeTests(unittest.TestCase):
    """
    This is negative test case for the function mean from the module stats.
    """
    def test_not_a_list(self):
        """
        This test checks if the function deals correctly with not a list argument.
        """
        with self.assertRaises(TypeError) as error:
            mode('a')
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')

    def test_not_numeric_values_in_list(self):
        """
        This test checks if the function deals correctly with list with not numeric values given as an argument.
        """
        with self.assertRaises(TypeError) as error:
            mode([1, 'a'])
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')
