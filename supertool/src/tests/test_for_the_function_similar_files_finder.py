"""
This is a unittest test suite for the function similar_files_finder from the module similar_files_finder.
"""

import unittest
import os
import sys

from supertool.similar_files_finder import similar_files_finder
from supertool.io_redirect import StdOutRedirector

PATH = os.path.abspath(os.path.dirname(__file__))


class PositiveTest(unittest.TestCase):
    """
    This is test case contains the positive tests for the function similar_files_finder from the module
    similar_files_finder
    """
    def test_two_similar_files_in_the_same_directory(self):
        """
        This test checks if the function correctly finds two similar files in the same directory.
        """
        test_dir = os.path.join(PATH, 'TEST_FILES', 'test1')
        os.makedirs(test_dir, exist_ok=True)
        with open(os.path.join(test_dir, 'file1.txt'), 'w') as file:
            print('abacaba', file=file)
        with open(os.path.join(test_dir, 'file2.txt'), 'w') as file:
            print('abacaba', file=file)

        with StdOutRedirector():
            similar_files_finder(test_dir)
            self.assertEqual(sys.stdout.getvalue(),
                             "Looking for similar files in directory: {}\n"
                             "These 2 files have similar contents: \n"
                             "    file1.txt\n"
                             "    file2.txt\n".format(os.path.join(PATH, test_dir)))

    def test_two_similar_files_in_different_directories(self):
        """
        This test checks if the function correctly finds two similar files in different directories.
        """
        test_dir = os.path.join(PATH, 'TEST_FILES', 'test2')
        os.makedirs(test_dir, exist_ok=True)
        with open(os.path.join(test_dir, 'file1.txt'), 'w') as file:
            print('abacaba', file=file)

        test_sub_dir = os.path.join(test_dir, 'sub_dir')
        os.makedirs(test_sub_dir, exist_ok=True)
        with open(os.path.join(test_sub_dir, 'file2.txt'), 'w') as file:
            print('abacaba', file=file)

        with StdOutRedirector():
            similar_files_finder(os.path.join(PATH, test_dir))
            self.assertEqual(sys.stdout.getvalue(),
                             "Looking for similar files in directory: {}\n"
                             "These 2 files have similar contents: \n"
                             "    file1.txt\n"
                             "    sub_dir\\file2.txt\n".format(os.path.join(PATH, test_dir)))

    def test_four_files_in_different_directories(self):
        """
        This tests checks if the function correctly finds two pairs of similar files in different directories.
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

        with StdOutRedirector():
            similar_files_finder(os.path.join(PATH, test_dir))
            self.assertEqual(sys.stdout.getvalue(),
                             "Looking for similar files in directory: {}\n"
                             "These 2 files have similar contents: \n"
                             "    file1.txt\n"
                             "    sub_dir\\file3.txt\n"
                             "These 2 files have similar contents: \n"
                             "    file2.py\n"
                             "    sub_dir\\file4.md\n".format(os.path.join(PATH, test_dir)))

    def test_empty_directory(self):
        """
        This test checks if the function correctly finds no similar files in the empty directory.
        """
        test_dir = os.path.join(PATH, 'TEST_FILES', 'test4')
        os.makedirs(test_dir, exist_ok=True)
        with StdOutRedirector():
            similar_files_finder(test_dir)
            self.assertEqual(sys.stdout.getvalue(), 'Looking for similar files in directory: {}\n'
                                                    'No similar files found.\n'.format(os.path.abspath(test_dir)))


class NegativeTests(unittest.TestCase):
    """
    This is test case contains the negative tests for the function similar_files_finder from the module
    similar_files_finder
    """
    def test_not_existing_directory(self):
        """
        This test checks if the function deals correctly with the situation when given directory does not exist.
        """
        with self.assertRaises(ValueError) as error:
            similar_files_finder('aJBJHBDAHJSBjhsabdjhbashdabjahw')
        self.assertEqual(error.exception.args[0], "such directory does not exist.")


if __name__ == '__main__':
    unittest.main()
