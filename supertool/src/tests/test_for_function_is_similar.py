"""
This is a unittest test suite for the function is_similar from the module similar_files_finder.
"""

import unittest
import os

from supertool.similar_files_finder import is_similar

PATH = os.path.abspath(os.path.dirname(__file__))


class PositiveTests(unittest.TestCase):
    """
    This test case contains the positive tests for the function is_similar from the module similar_files_finder.
    """
    def test_two_similar_files_in_the_same_directory(self):
        """
        This test checks if function works correctly for the two similar files in the same directory.
        """
        test_dir = os.path.join(PATH, 'TEST_FILES', 'test1')
        os.makedirs(test_dir, exist_ok=True)
        with open(os.path.join(test_dir, 'file1.txt'), 'w') as file:
            print('abacaba', file=file)
        with open(os.path.join(test_dir, 'file2.txt'), 'w') as file:
            print('abacaba', file=file)
        self.assertTrue(is_similar(os.path.join(test_dir, 'file1.txt'), os.path.join(test_dir, 'file2.txt')))

    def test_two_different_files(self):
        """
        This test checks if the function works correctly for the two different files in the same directory.
        """
        test_dir = os.path.join(PATH, 'TEST_FILES', 'test1')
        os.makedirs(test_dir, exist_ok=True)
        with open(os.path.join(test_dir, 'file1.txt'), 'w') as file:
            print('abacaba1', file=file)
        with open(os.path.join(test_dir, 'file2.txt'), 'w') as file:
            print('abacaba', file=file)
        self.assertFalse(is_similar(os.path.join(test_dir, 'file1.txt'), os.path.join(test_dir, 'file2.txt')))

    def test_two_similar_files_in_different_directories(self):
        """
        This test checks if the function works correctly for the two similar files in different directories.
        """
        test_dir = os.path.join(PATH, 'TEST_FILES', 'test2')
        os.makedirs(test_dir, exist_ok=True)
        with open(os.path.join(test_dir, 'file1.txt'), 'w') as file:
            print('abacaba', file=file)
        test_sub_dir = os.path.join(test_dir, 'sub_dir')
        os.makedirs(test_sub_dir, exist_ok=True)
        with open(os.path.join(test_sub_dir, 'file2.txt'), 'w') as file:
            print('abacaba', file=file)
        self.assertTrue(is_similar(os.path.join(test_dir, 'file1.txt'), os.path.join(test_sub_dir, 'file2.txt')))


class NegativeTests(unittest.TestCase):
    def test_file_not_found(self):
        """
        This function checks if the function correctly deals with the situation when one of the given files does not
        exist.
        """
        test_dir = os.path.join(PATH, 'TEST_FILES', 'test1')
        os.makedirs(test_dir, exist_ok=True)
        with open(os.path.join(test_dir, 'file1.txt'), 'w') as file:
            print('abacaba', file=file)
        with self.assertRaises(FileNotFoundError) as error:
            is_similar(os.path.join(test_dir, 'file1.txt'), os.path.join(test_dir, 'file3.txt'))
        self.assertEqual(error.exception.args[0], 'arguments of the function should be two existing files.')


if __name__ == '__main__':
    unittest.main()