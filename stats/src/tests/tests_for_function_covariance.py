"""
This is a unittest test suite for the function covariance from the module stats.stats.
"""
import unittest
from stats.stats import covariance


class PositiveTests(unittest.TestCase):
    """
    This is positive test case for the function covariance from the module stats.
    """
    def test_similar_samples(self):
        """
        This test checks if the function deals correctly with samples [1, 2, 3] and [1, 2, 3].
        """
        self.assertAlmostEqual(covariance([1, 2, 3], [1, 2, 3]), 0.6666666666666666, delta=0.0001)

    def test_linear_samples(self):
        """
        This test checks if the function deals correctly with samples [1, 2, 3, 4, 5, 6, 7] and
        [2, 4, 6, 8, 10, 12, 14].
        """
        self.assertEqual(covariance([1, 2, 3, 4, 5, 6, 7], [2, 4, 6, 8, 10, 12, 14]), 8.0)

    def test_random_samples(self):
        """
        This test checks if the function deals correctly with samples [1.21, 3.45, -7.3] and [-2.41, 1.26, -1].
        """
        self.assertAlmostEqual(covariance([1.21, 3.45, -7.3], [-2.41, 1.26, -1]), 2.279633333333333, delta=0.0001)

    def test_zero_length_argument(self):
        """
        This test checks if the function deals correctly with samples [] and [1].
        """
        self.assertEqual(covariance([], [1]), 0)


class NegativeTests(unittest.TestCase):
    """
    This is negative test case for the function covariance from the module stats.
    """
    def test_not_equal_length(self):
        """
        This test checks if the function deals correctly with argument lists of not equal length.
        """
        with self.assertRaises(ValueError) as error:
            covariance([1], [1, 2])
        self.assertEqual(error.exception.args[0], 'vectors must have equal length')

    def test_not_a_list(self):
        """
        This test checks if the function deals correctly with not a list argument.
        """
        with self.assertRaises(TypeError) as error:
            covariance('a', 1)
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')

    def test_not_numeric_values_in_list(self):
        """
        This test checks if the function deals correctly with list with not numeric values given as an argument.
        """
        with self.assertRaises(TypeError) as error:
            covariance([1, 'a'], [1, 2])
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')