"""
This is a unittest test suite for the function std from the module stats.stats.
"""
import unittest
from stats.stats import std


class PositiveTests(unittest.TestCase):
    """
    This is positive test case for the function std from the module stats.
    """
    def test_one_element(self):
        """
        This test checks if the function deals correctly with list of one element.
        """
        self.assertEqual(std([1]), 0.0)

    def test_simple_int_list(self):
        """
        This test checks if the function deals correctly with list [1, 2, 3, 4, 5].
        """
        self.assertAlmostEqual(std([1, 2, 3, 4, 5]), 1.4142135623730951, delta=0.0001)

    def test_harder_test(self):
        """
        This test checks if the function deals correctly with list [1.21, -3.42, 5.56, 112.86, -34].
        """
        self.assertAlmostEqual(std([1.21, -3.42, 5.56, 112.86, -34]), 50.17122059507821, delta=0.0001)


class NegativeTests(unittest.TestCase):
    """
    This is negative test case for the function std from the module stats.
    """
    def test_not_a_list(self):
        """
        This test checks if the function deals correctly with not a list argument.
        """
        with self.assertRaises(TypeError) as error:
            std('a')
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')

    def test_not_numeric_values_in_list(self):
        """
        This test checks if the function deals correctly with list with not numeric values given as an argument.
        """
        with self.assertRaises(TypeError) as error:
            std([1, 'a'])
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')
