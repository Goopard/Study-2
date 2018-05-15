"""
This is a unittest test suite for the function correlation from the module stats.stats.
"""
import unittest
from stats.stats import correlation


class PositiveTests(unittest.TestCase):
    """
    This is positive test case for the function correlation from the module stats.
    """
    def test_similar_samples(self):
        """
        This test checks if the function deals correctly with samples [1, 2, 3] and [1, 2, 3].
        """
        self.assertEqual(correlation([1, 2, 3], [1, 2, 3]), 1.0)

    def test_linear_samples(self):
        """
        This test checks if the function deals correctly with samples [1, 2, 3, 4, 5, 6, 7] and
        [2, 4, 6, 8, 10, 12, 14].
        """
        self.assertEqual(correlation([1, 2, 3, 4, 5, 6, 7], [2, 4, 6, 8, 10, 12, 14]), 1.0)

    def test_quad_samples(self):
        """
        This test checks if the function deals correctly with samples [1.21, 3.45, -7.3] and [-2.41, 1.26, -1].
        """
        self.assertAlmostEqual(correlation([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]), 0.9811049102515927, delta=0.001)

    def test_fifth_degree_samples(self):
        """
        This test checks if the function deals correctly with samples [1.21, 3.45, -7.3] and [-2.41, 1.26, -1].
        """
        self.assertAlmostEqual(correlation([1, 2, 3, 4, 5], [1, 32, 243, 1024, 3125]), 0.8679439350990682, delta=0.001)

    def test_zero_std_x(self):
        """
        This test checks if the function deals correctly with samples [1] and [1].
        """
        self.assertEqual(correlation([1], [1]), 0)


class NegativeTests(unittest.TestCase):
    """
    This is negative test case for the function correlation from the module stats.
    """
    def test_not_equal_length(self):
        """
        This test checks if the function deals correctly with argument lists of not equal length.
        """
        with self.assertRaises(ValueError) as error:
            correlation([1, 1, 1, 2, 5, 6, 7, 2, 3], [1, 2, 8, 5, 2, 3])
        self.assertEqual(error.exception.args[0], 'vectors must have equal length')

    def test_not_a_list(self):
        """
        This test checks if the function deals correctly with not a list argument.
        """
        with self.assertRaises(TypeError) as error:
            correlation('a', 1)
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')

    def test_not_numeric_values_in_list(self):
        """
        This test checks if the function deals correctly with list with not numeric values given as an argument.
        """
        with self.assertRaises(TypeError) as error:
            correlation([1, 'a'], [1, 2])
        self.assertEqual(error.exception.args[0], 'argument of the function must be a list of values of type int '
                                                  'or float')