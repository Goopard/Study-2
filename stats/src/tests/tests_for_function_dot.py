"""
This is a unittest test suite for the function dot from the module stats.stats.
"""
import unittest
from stats.stats import dot


class PositiveTests(unittest.TestCase):
    """
    This is positive test case for the function dot from the module stats.
    """
    def test_vectors_of_length_1(self):
        """
        This test checks if the function deals correctly with vectors [1] and [1].
        """
        self.assertEqual(dot([1], [1]), 1)

    def test_vectors_of_length_3(self):
        """
        This test checks if the function deals correctly with vectors [1, 1, 2] and [2, 1, 3].
        """
        self.assertEqual(dot([1, 1, 2], [2, 1, 3]), 9)

    def test_harder_vectors_of_length_3(self):
        """
        This test checks if the function deals correctly with vectors [1.21, 3.45, -7.3] and [-2.41, 1.26, -1].
        """
        self.assertAlmostEqual(dot([1.21, 3.45, -7.3], [-2.41, 1.26, -1]), 8.7309, delta=0.0001)


class NegativeTests(unittest.TestCase):
    """
    This is negative test case for the function dot from the module stats.
    """
    def test_not_equal_length(self):
        """
        This test checks if the function deals correctly with argument lists of not equal length.
        """
        with self.assertRaises(ValueError) as error:
            dot([1], [1, 2])
        self.assertEqual(error.exception.args[0], 'vectors must have equal length')

    def test_not_a_list(self):
        """
        This test checks if the function deals correctly with not a list argument.
        """
        with self.assertRaises(TypeError) as error:
            dot('a', 1)
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')

    def test_not_numeric_values_in_list(self):
        """
        This test checks if the function deals correctly with list with not numeric values given as an argument.
        """
        with self.assertRaises(TypeError) as error:
            dot([1, 'a'], [1, 2])
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')