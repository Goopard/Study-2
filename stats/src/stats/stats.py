"""
This module contains functions for statical analysis of data.
"""

import math
from stats.base import check_numeric
from collections import Counter


def mean(x):
    """Returns a mean value of some list of numeric values x ignoring NaN values.

    :param x: List of numeric values.
    :type x: list.
    :return: float -- The required mean value.
    """
    check_numeric(x)
    return sum([i for i in x if not math.isnan(i)]) / len(x)


def median(x):
    """Counts a median of some list of numeric values ignoring NaN values.

    :param x: List of numeric values.
    :type x: list.
    :return: float -- The required median.
    """
    check_numeric(x)
    x_sorted = [i for i in sorted(x) if not math.isnan(i)]
    if len(x) % 2:
        return x_sorted[len(x) // 2]
    else:
        return (x_sorted[len(x) // 2] + x_sorted[len(x) // 2 - 1]) / 2


def mode(x):
    """Counts mode values of some list of numeric values.

    :param x: List of numeric values.
    :type x: list.
    :return: list[float] -- List of mode values.
    """
    check_numeric(x)
    counts = Counter(x)
    max_val = max(counts.values())
    return [key for key, count in counts.items() if count == max_val]


def quantile(x, p):
    """Counts a p-quantile of sample x.

    :param x: Sample (list of numeric values).
    :type x: list.
    :param p: Probability of the quantile.
    :type p: float.
    :return: float -- The required quantile.
    """
    if p >= 1 or p < 0:
        raise ValueError('argument p should be more then 0 and less then 1')
    check_numeric(x)
    p_idx = int(p * len(x))
    return sorted(x)[p_idx]


def variance(x):
    """Counts a variance of some list of numeric values.

    :param x: List of numeric values.
    :type x: list.
    :return: float -- The required variance.
    """
    check_numeric(x)
    m = mean(x)
    return sum([(d - m) ** 2 for d in x]) / len(x)


def std(x):
    """Counts standard deviation of some list of numeric values.

    :param x: List of numeric values.
    :type x: list.
    :return: float -- The required standard deviation.
    """
    return variance(x) ** 0.5


def dot(x, y):
    """Counts the dot product of two vectors (lists of numeric values) of equal length.

    :param x: First vector.
    :type x: list.
    :param y: Second vector.
    :type y: list.
    :return: float -- The required dot product.
    """
    check_numeric(x)
    check_numeric(y)
    if len(x) == len(y):
        return sum([i * j for i, j in zip(x, y)])
    raise ValueError('vectors must have equal length')


def covariance(x, y):
    """Counts the covariance of two samples (lists of numeric values) of equal length.

    :param x: First sample.
    :type x: list.
    :param y: Second sample.
    :type y: list.
    :return: float -- The required covariance.
    """
    if len(x) == 0:
        return 0
    m_x = mean(x)
    m_y = mean(y)
    dev_x = [i - m_x for i in x]
    dev_y = [i - m_y for i in y]
    return dot(dev_x, dev_y) / len(x)


def correlation(x, y):
    """Counts the correlation of two samples (lists of numeric values).

    :param x: First sample.
    :type x: list.
    :param y: Second sample.
    :type y: list.
    :return: float -- The required correlation value.
    """
    std_x = std(x)
    std_y = std(y)
    if std_x > 0 and std_y > 0:
        return covariance(x, y) / std_x / std_y
    return 0


def data_range(x):
    """Counts data range of some data list x.

    :param x: List of numeric values.
    :type x: list.
    :return: float -- The required data range.
    """
    check_numeric(x)
    return max(x) - min(x)
