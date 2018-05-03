"""
This is a unittest test suite for the function files_finder in the module similar_files_finder.
"""

import unittest
import os

from supertool.similar_files_finder import files_finder

PATH = os.path.abspath(os.path.dirname(__file__))


class PositiveTests(unittest.TestCase):
    """
    This test case contains the positive tests for the function files_finder.
    """
    def test_two_files_in_the_same_directory(self):
        """
        This tests checks if the function is working correctly for the directory containing two files.
        """
        test_dir = os.path.join(PATH, 'TEST_FILES', 'test1')
        os.makedirs(test_dir, exist_ok=True)
        with open(os.path.join(test_dir, 'file1.txt'), 'w') as file:
            print('abacaba', file=file)
        with open(os.path.join(test_dir, 'file2.txt'), 'w') as file:
            print('abacaba', file=file)

        files = files_finder(test_dir)
        self.assertEqual([file.name for file in files], ['file1.txt', 'file2.txt'])

    def test_four_files_in_different_directories(self):
        """
        This test checks if the function is working correctly for the directory with two files and a subdirectory with
        another two files.
        """
        test_dir = os.path.join(PATH, 'TEST_FILES', 'test3')
        os.makedirs(test_dir, exist_ok=True)
        with open(os.path.join(test_dir, 'file1.txt'), 'w') as file:
            print('abacaba', file=file)
        with open(os.path.join(test_dir, 'file2.py'), 'w') as file:
            print('abacaba123', file=file)

        test_sub_dir = os.path.join(test_dir, 'sub_dir')
        os.makedirs(test_sub_dir, exist_ok=True)
        with open(os.path.join(test_sub_dir, 'file3.txt'), 'w') as file:
            print('abacaba', file=file)
        with open(os.path.join(test_sub_dir, 'file4.md'), 'w') as file:
            print('abacaba123', file=file)

        files = files_finder(test_dir)
        self.assertEqual([file.name for file in files], ['file1.txt', 'file2.py', 'file3.txt', 'file4.md'])


class NegativeTests(unittest.TestCase):
    def test_not_existing_directory(self):
        """
        This test checks if the function deals correctly with not existing directory given as an argument.
        """
        with self.assertRaises(FileNotFoundError) as error:
            files_finder('kjahdbfhbadsjhfbasdjhfb')
        self.assertEqual(error.exception.args[0], 'such directory does not exist')


if __name__ == '__main__':
    unittest.main()