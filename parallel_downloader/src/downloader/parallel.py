"""
This module contains the functions for parallel download of some images.
"""

import os
import time
from io import BytesIO

import requests
from PIL import Image

from multiprocessing.pool import ThreadPool


def get_size(size):
    """This function transforms the size of an image from str to tuple of two integers or returns (100, 100) if size ==
    None.

    :param size: Size in str format.
    :type size: str or None.
    :return: Tuple or None -- size stored as a tuple of two integers or None if the input data was incorrect.
    """
    if not size:
        return tuple([100, 100])
    size = size.split(sep='x')
    if not len(size) == 2:
        print("Argument --size should be two ints separated by letter 'x' (i.eg. 100x100)!")
        return None
    try:
        size[0] = int(size[0])
        size[1] = int(size[1])
    except TypeError:
        print("Argument --size should be two ints separated by letter 'x' (i.eg. 100x100)!")
        return None
    return tuple(size)


def get_dir_path(dir_path):
    """This function creates a directory with a path dir_path if it does not exist (with all subdirectories), or, if
    dir_path == None, it sets dir_path as '.'.

    :param dir_path: Path to a directory.
    :type dir_path: str or None.
    :return: str -- Same path as the given one or '.' if None was given.
    """
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = '.'
    return dir_path


def get_num_threads(num_threads):
    """This function transforms num_threads to an integer if it was given as some str or sets it as 1 if
    num_threads was given as None.

    :param num_threads: Number of threads given as str or None.
    :type num_threads: str or None.
    :return: int or None -- Number of threads or None if some error occurred.
    """
    if not num_threads:
        num_threads = 1
    else:
        try:
            num_threads = int(num_threads)
        except ValueError:
            print('Argument --threads should be int!')
            return None
    return num_threads


def check_params(path, dir_path, num_threads, size):
    """This function checks if all the parameters of the function download_from_file are correct and tries to make them
    correct otherwise.

    :param path: Path to the file with urls.
    :type path: str.
    :param dir_path: Path to the downloading directory.
    :type dir_path: str or None.
    :param num_threads: Number of threads.
    :type num_threads: str or None.
    :param size: Size of the images.
    :type size: str or None.
    :return: Tuple or None -- New values of dir_path, num_threads, size or None if something went wrong.
    """
    if not os.path.exists(path) or not os.path.isfile(path):
        print('Wrong path to the file with urls!')
        return None
    dir_path = get_dir_path(dir_path)
    num_threads = get_num_threads(num_threads)
    size = get_size(size)
    if not num_threads or not size:
        return None
    return dir_path, num_threads, size


NUM_OK = 0
TOTAL_BYTES = 0


def download_image(url, name, dir_path, size):
    """This function downloads an image and formats it.

    :param url: Url of the image.
    :type url: str.
    :param name: Name that will be given to the image.
    :type name: any.
    :param dir_path: Path to the directory where image will be downloaded to.
    :type dir_path: str.
    :param size: Size that image will be formatted to.
    :type size: Tuple.
    :return: None
    """
    response = requests.get(url)
    if response.headers['content-type'] == 'image/jpeg':
        image = Image.open(BytesIO(response.content))
        image.thumbnail(size)
        image.save(os.path.join(dir_path, '{}.jpeg'.format(name)), 'JPEG')
        print('Image {}.jpeg downloaded with size: {}!'.format(name, size))
        global NUM_OK, TOTAL_BYTES
        NUM_OK += 1
        TOTAL_BYTES += len(response.content)


def download_from_file(path, dir_path, num_threads, size):
    """This function downloads all the images from some .txt file with urls of those images to some downloading
    directory in parallel with some given number of threads.

    :param path: Path to the file with urls.
    :type path: str.
    :param dir_path: Path to the target directory.
    :type dir_path: str or None.
    :param num_threads: Number of threads.
    :type num_threads: str or None.
    :param size: Size that images will be formatted to.
    :type size: str or None.
    :return: None.
    """
    try:
        dir_path, num_threads, size = check_params(path, dir_path, num_threads, size)
    except TypeError:
        return None
    time_start = time.time()
    downloading_pool = ThreadPool(num_threads)
    url_file = open(path, 'r')
    urls = url_file.read().splitlines()
    i = 1
    for url in urls:
        downloading_pool.apply_async(download_image, args=tuple([url, i, dir_path, size]))
        i += 1
    downloading_pool.close()
    downloading_pool.join()
    print("\nTime elapsed: {} seconds\n".format(time.time() - time_start),
          "Downloaded {} files\n".format(NUM_OK),
          "Errors occurred on {} entries in {}\n".format(len(urls) - NUM_OK, path),
          "Total bytes downloaded: {}".format(TOTAL_BYTES))
