"""
This module contains functions used to find similar files in some directory.
"""

import os


class FileWithHash:
    """
    This class is used store the files with their hashes.
    """
    def __init__(self, file):
        """Constructor of the class File, counts the hash of the file.

        :param file: File.
        :type file: os.DirEntry.
        """
        self.path = file.path
        self.name = file.name
        try:
            with open(file.path, 'r') as file_contents:
                self.hash = file_contents.read().__hash__()
        except UnicodeDecodeError:
            self.hash = None


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
            files.append(FileWithHash(file))
        if file.is_dir():
            files += files_finder(file.path)
    return files


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
            if file.hash == chain[0].hash:
                chain.append(file)
                break
        else:
            buffer.append([file])
    file_chains = [chain for chain in buffer if len(chain) > 1 and chain[0].hash]
    return file_chains


def similar_files_finder(directory):
    """This function finds all the chains of similar files in the given directory and prints them.

    :param directory: Path to the directory.
    :type directory: str.
    :return: None.
    """
    print('Looking for similar files in directory: {}'.format(os.path.abspath(directory)))
    file_chains = similar_files_chains(directory)
    if not len(file_chains):
        print('No similar files found.')
    for chain in file_chains:
        print('These {} files have similar contents: '.format(len(chain)))
        for file in chain:
            print('   ', os.path.relpath(file.path, directory))
