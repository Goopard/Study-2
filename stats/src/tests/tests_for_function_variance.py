"""
This is a unittest test suite for the function variance from the module stats.stats.
"""
import unittest
from stats.stats import variance


class PositiveTests(unittest.TestCase):
    """
    This is positive test case for the function variance from the module stats.
    """
    def test_one_element(self):
        """
        This test checks if the function deals correctly with list of one element.
        """
        self.assertEqual(variance([1]), 0.0)

    def test_simple_int_list(self):
        """
        This test checks if the function deals correctly with list [1, 2, 3, 4, 5].
        """
        self.assertEqual(variance([1, 2, 3, 4, 5]), 2.0)

    def test_harder_test(self):
        """
        This test checks if the function deals correctly with list [1.21, -3.42, 5.56, 112.86, -34].
        """
        self.assertAlmostEqual(variance([1.21, -3.42, 5.56, 112.86, -34]), 2517.1513760000003, delta=0.0001)


class NegativeTests(unittest.TestCase):
    """
    This is negative test case for the function variance from the module stats.
    """
    def test_not_a_list(self):
        """
        This test checks if the function deals correctly with not a list argument.
        """
        with self.assertRaises(TypeError) as error:
            variance('a')
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')

    def test_not_numeric_values_in_list(self):
        """
        This test checks if the function deals correctly with list with not numeric values given as an argument.
        """
        with self.assertRaises(TypeError) as error:
            variance([1, 'a'])
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')
