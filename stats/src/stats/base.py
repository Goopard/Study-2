"""
This module contains functions for downloading, reading, validation and some modifying of data.
"""

import math
import urllib.request
import csv
import codecs


def isnumeric(x):
    """Checks if variable x (or all values in x if x is iterable) has numeric type.

    :param x: Some variable.
    :type x: any.
    :return: bool
    """
    try:
        return all(isinstance(i, (float, int)) for i in x)
    except TypeError:
        return isinstance(x, (float, int))


def make_numeric(x, numeric_type=float):
    """This function tries to cast all the values in x to some numeric type. If it fails, it just returns the original
    list.

    :param x: List.
    :type x: list.
    :param numeric_type: Type values of x will be casted to. Can only be int or float.
    :return list -- new list of numeric values on success and just the same list x otherwise.
    """
    result = []
    if numeric_type not in (float, int):
        raise ValueError("argument numeric_type can only have value <class 'int'> or <class 'float'>")
    try:
        for elem in x:
            if elem == '':
                result.append(float('NaN'))
            else:
                result.append(numeric_type(elem))
        return result
    except (ValueError, TypeError):
        return x


def check_numeric(x):
    """This function checks if given list only contains numeric values and raises an exception if this is not true.

    :param x: List.
    :type x: list.
    """
    if not (isnumeric(x) and isinstance(x, list)):
        raise TypeError('argument of the function must be a list of values of type int or float')


def download_csv(url):
    """Downloads a .csv file from some url and returns its contents as a list of rows.

    :param url: Url of the .csv file.
    :type url: str.
    :return: list[list] -- Contents of the .csv file as a list of rows.
    """
    url_data = urllib.request.urlopen(url)
    reader = csv.reader(codecs.iterdecode(url_data, 'utf-8'))
    data_list = []
    for row in reader:
        data_list.append(row)
    return data_list


def read_csv(path):
    """Reads some .csv using some path and returns its contents as a list of rows.

    :param path: Path to the .csv file.
    :type path: str.
    :return: list[list] -- List of rows of .csv file.
    """
    with open(path, 'r') as csv_file:
        data_list = [line.split(sep=',') for line in csv_file.read().splitlines()]
        return data_list


def make_columns(data_list):
    """Reformats given data_list to a dict of columns {column name: [values]}, where column names are taken from the
    first row of the data_list.

    :param data_list: Some downloaded .csv file given as a list of rows given as lists.
    :type data_list: list[list]
    :return: dict{list} -- Given data_list reformatted to a dict of columns.
    """
    try:
        n = len(data_list[0])
    except IndexError:
        return {}
    try:
        data = {data_list[0][i]: [data_list[j][i] for j in range(1, len(data_list))] for i in range(n)}
    except IndexError:
        raise ValueError('rows in data_list must have equal lengths')
    return data


def fill_nan(x, value):
    """Fills all the NaN values in sample x with argument value.

    :param x: Sample (list of numeric type).
    :type x: list.
    :param value: Fillvalue.
    :type value: float or int.
    :return: list -- x with nan values replaced with value.
    """
    return [i if not math.isnan(i) else value for i in x]
