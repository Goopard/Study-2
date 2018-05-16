"""
This module contains functions used to find similar files in some directory.
"""

import os


def files_finder(directory):
    """This function finds all the files in the given directory (and all subdirectories) and returns them as a list of
    os.DirEntry objects.

    :param directory: Path to the directory.
    :return: list(os.DirEntry).
    """
    if not os.path.exists(directory):
        raise FileNotFoundError('such directory does not exist')
    files = []
    for file in os.scandir(directory):
        if file.is_file():
            files.append(file)
        if file.is_dir():
            files += files_finder(file.path)
    return files


def is_similar(path1, path2):
    """This functions checks if the two files given as absolute paths have the same contents.

    :param path1: Path to the first file.
    :type path1: str.
    :param path2: Path to the second file.
    :type path2: str.
    :return: bool.
    """
    if not (os.path.exists(path1) and os.path.exists(path2)):
        raise FileNotFoundError('arguments of the function should be two existing files.')
    with open(path1, 'r') as file1:
        with open(path2, 'r') as file2:
            contents1 = file1.read()
            contents2 = file2.read()
            return contents1 == contents2


def similar_files_chains(directory):
    """This function finds all the chains of similar files in the given directory.

    :param directory: Path to the directory.
    :type directory: str.
    :return: list[list] -- List of the required file chains given as lists.
    """
    directory = os.path.abspath(directory)
    if not os.path.exists(directory):
        raise ValueError('such directory does not exist.')
    files = files_finder(directory)
    buffer = []
    for file in files:
        for chain in buffer:
            if is_similar(file, chain[0]):
                chain.append(file)
                break
        else:
            buffer.append([file])
    file_chains = [chain for chain in buffer if len(chain) > 1]
    return file_chains


def similar_files_finder(directory):
    """This function finds all the chains of similar files in the given directory and prints them.

    :param directory: Path to the directory.
    :type directory: str.
    :return: None.
    """
    print('Looking for similar files in directory: {}'.format(directory))
    file_chains = similar_files_chains(directory)
    if not len(file_chains):
        print('No similar files found.')
    for chain in file_chains:
        print('These {} files have similar contents: '.format(len(chain)))
        for file in chain:
            print('   ', os.path.relpath(file.path, directory))

