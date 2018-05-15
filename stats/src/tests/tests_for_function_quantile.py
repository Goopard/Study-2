"""
This is a unittest test suite for the function quantile from the module stats.stats.
"""
import unittest
from stats.stats import quantile


class PositiveTests(unittest.TestCase):
    """
    This is positive test case for the function quantile from the module stats.
    """
    def test_one_element(self):
        """
        This test checks if the function deals correctly with list of one element.
        """
        self.assertEqual(quantile([1], 0.5), 1)

    def test_simple_int_list(self):
        """
        This test checks if the function deals correctly with list [1, 2, 3, 4, 5].
        """
        self.assertEqual(quantile([1, 2, 3, 4, 5], 0.2), 2)

    def test_list_of_float(self):
        """
        This test checks if the function deals correctly with list [1.21, -3.42, 5.56, 112.86, -34].
        """
        self.assertEqual(quantile([1.21, -3.42, 5.56, 112.86, -34], 0.75), 5.56)


class NegativeTests(unittest.TestCase):
    """
    This is negative test case for the function quantile from the module stats.
    """
    def test_not_a_list(self):
        """
        This test checks if the function deals correctly with not a list argument.
        """
        with self.assertRaises(TypeError) as error:
            quantile('a', 0.5)
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')

    def test_not_numeric_values_in_list(self):
        """
        This test checks if the function deals correctly with list with not numeric values given as an argument.
        """
        with self.assertRaises(TypeError) as error:
            quantile([1, 'a'], 0.5)
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')

    def test_wrong_p(self):
        """
        This test checks if the function deals correctly with list with argument p > 1.
        """
        with self.assertRaises(ValueError) as error:
            quantile([1, 2], 10)
        self.assertEqual(error.exception.args[0], 'argument p should be more then 0 and less then 1')
