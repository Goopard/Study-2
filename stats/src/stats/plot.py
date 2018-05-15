"""
This module contains plotting functions of the module stats.
"""
import matplotlib.pyplot as plt
import math
from collections import Counter
from stats.base import check_numeric


def make_buckets(x, bucket_size):
    """Divides the sample x into some buckets of size bucket_size.

    :param x: Sample (list of numeric values).
    :type x: list.
    :param bucket_size: Size of the bucket.
    :type bucket_size: int.
    :return: Counter -- x divided into buckets.
    """
    check_numeric(x)
    return Counter([bucket_size * math.floor(i / bucket_size) for i in x if not math.isnan(i)])


def hist(x, bucket_size, xlabel="", ylabel="", title=""):
    """Creates and shows a histogram for some sample x with the bucket size bucket_size.

    :param x: Sample (list of numeric values).
    :type x: list.
    :param bucket_size: Size of the buckets.
    :type bucket_size: int.
    :param xlabel: Label of the x axis.
    :type xlabel: str.
    :param ylabel: Label of the y axis.
    :type ylabel: str.
    :param title: Title of the histogram.
    :type title: str.
    """
    hist_data = make_buckets(x, bucket_size)
    plt.bar(hist_data.keys(), hist_data.values(), width=bucket_size)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def plot(*args, **kwargs):
    """
    Just a copy of matplotlib.pyplot.plot().
    """
    plt.plot(*args, **kwargs)
    plt.show()


def box_plot(*args, **kwargs):
    """
    Just a copy of matplotlib.pyplor.boxplot().
    """
    plt.boxplot(*args, **kwargs)
