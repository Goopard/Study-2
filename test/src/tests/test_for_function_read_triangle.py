import unittest
import sys
import io

from ..triangle.square_counter import read_triangle


class StdInRedirector:
    def __init__(self, args):
        self.args = args

    def __enter__(self):
        self.old_stdin = sys.stdin
        sys.stdin = io.StringIO(self.args)

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdin = self.old_stdin


class Tests(unittest.TestCase):
    def test_entered_from_the_first_try(self):
        with StdInRedirector('1 2\n1 2\n1 2\n'):
            self.assertEqual(read_triangle(), [1.0, 2.0, 1.0, 2.0, 1.0, 2.0])

    def test_entered_from_the_second_try_because_of_too_many_coordinates(self):
        with StdInRedirector('1 2 3\n1 2\n1 2\n1 2\n'):
            self.assertEqual(read_triangle(), [1.0, 2.0, 1.0, 2.0, 1.0, 2.0])

    def test_entered_from_the_second_try_because_of_wrong_type(self):
        with StdInRedirector('1 a\n1 2\n1 2\n1 2\n'):
            self.assertEqual(read_triangle(), [1.0, 2.0, 1.0, 2.0, 1.0, 2.0])

    def test_entered_from_the_second_try_because_of_too_few_coordinates(self):
        with StdInRedirector('\n1 2\n1 2\n1 2\n'):
            self.assertEqual(read_triangle(), [1.0, 2.0, 1.0, 2.0, 1.0, 2.0])


if __name__ == '__main__':
    unittest.main()
