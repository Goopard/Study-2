"""
This module contains the functions for counting the are of triangle.
"""

# Комментарий по поводу того, что все функции у меня принимают *args: ты на лекции говорил, что надо исходить из того,
# что пользователь совсем не соображает, поэтому я предположил, что он мог бы ввести какое-то неправильное количество
# аргументов => он в таком случае должен получать не эксепшн с трейсбеком, а такую же текстовую ошибку, как и в других
# случаях. Поэтому тут так.


def distance(*args):
    """This function counts the distance between two dots given as lists of two coordinates each.

    Tests:
    Positive ones:
    >>> distance([1, 1], [1, 1])
    0.0
    >>> distance([1, 1], [0, 0])
    1.4142135623730951
    >>> distance([12.3, -54.178], [-45, 34.19])
    105.31948264210187

    Negative ones:
    >>> distance([1, 2, 3, 4], [1, 1])
    ERROR: two lists of 2 elements expected, got 4, 2.
    >>> distance([1, 1], 'a')
    ERROR: two lists of floats expected as arguments, got <class 'list'>, <class 'str'>.
    >>> distance([1, 'a'], [0, 0])
    ERROR: type int or float expected, got <class 'str'>.
    >>> distance()
    ERROR: two arguments expected, got 0.
    >>> distance([1, 1], [1, 1], [1, 1])
    ERROR: two arguments expected, got 3.

    :param args: Tuple of two dots, each one must be a list of two floats or ints.
    :type args: Tuple.
    :return: float -- The required distance.
    """
    if len(args) != 2:
        print('ERROR: two arguments expected, got {}.'.format(len(args)))
        return None
    dot1 = args[0]
    dot2 = args[1]
    if not (isinstance(dot1, list) and isinstance(dot2, list)):
        print('ERROR: two lists of floats expected as arguments, got {}, {}.'.format(type(dot1), type(dot2)))
        return None
    if len(dot1) != 2 or len(dot2) != 2:
        print('ERROR: two lists of 2 elements expected, got {}, {}.'.format(len(dot1), len(dot2)))
        return None
    for coordinate in dot1 + dot2:
        if not(isinstance(coordinate, (float, int))):
            print('ERROR: type int or float expected, got {}.'.format(type(coordinate)))
            return None
    return ((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2) ** 0.5


def area_of_triangle(*args):
    """This function counts the square of a triangle given as a list of 6 numbers - the coordinates of the vertexes.

    Tests:
    Positive ones:
    >>> area_of_triangle([0, 0, 1, 1, 0, 1])
    0.4999999999999998
    >>> area_of_triangle([1, 1, -1, -1, 0, 0])
    0.0
    >>> area_of_triangle([0, 0, 0, 0, 0, 0])
    0.0
    >>> area_of_triangle([1, 1, -1, -1, 1, -1])
    1.9999999999999991

    Negative ones:
    >>> area_of_triangle([0, 0])
    ERROR: 6 coordinates expected, got 2.
    >>> area_of_triangle([0, 0, 1, 2, 0, 'a'])
    ERROR: type int or float expected, got <class 'str'>.
    >>> area_of_triangle('a')
    ERROR: list of vertexes expected as an argument, got <class 'str'>.
    >>> area_of_triangle([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    ERROR: 6 coordinates expected, got 10.
    >>> area_of_triangle()
    ERROR: one argument expected, got 0.
    >>> area_of_triangle([1, 2, 3, 4, 5, 6], 'DFSFsfASFf')
    ERROR: one argument expected, got 2.

    :param vertexes: List of vertexes.
    :type vertexes: list(float or int): List of 6 elements of type int or float - the coordinates of the vertexes.
    :return: float -- Square of the triangle.
    """
    if len(args) != 1:
        print('ERROR: one argument expected, got {}.'.format(len(args)))
        return None
    vertexes = args[0]
    if not isinstance(vertexes, list):
        print('ERROR: list of vertexes expected as an argument, got {}.'.format(type(vertexes)))
        return None
    if len(vertexes) != 6:
        print('ERROR: 6 coordinates expected, got {}.'.format(len(vertexes)))
        return None
    for coordinate in vertexes:
        if not (isinstance(coordinate, int) or isinstance(coordinate, float)):
            print('ERROR: type int or float expected, got {}.'.format(type(coordinate)))
            return None
    ver = [[vertexes[0], vertexes[1]], [vertexes[2], vertexes[3]], [vertexes[4], vertexes[5]]]
    a = distance(ver[0], ver[1])
    b = distance(ver[1], ver[2])
    c = distance(ver[2], ver[0])
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def read_triangle():
    """This function reads the vertexes of the triangle.

    :return: list of float -- List of the coordinates of the vertexes of the triangle.
    """
    vertexes = []
    while len(vertexes) < 6:
        new_vertex = input('Please enter the coordinates of the vertex #{}: '
                           .format(int(len(vertexes) / 2 + 1))).split(sep=' ')
        if len(new_vertex) != 2:
            print('ERROR: vertex of the triangle should have exactly 2 coordinates!\nTry again.')
        else:
            try:
                new_vertex[0] = float(new_vertex[0])
                new_vertex[1] = float(new_vertex[1])
            except ValueError:
                print('ERROR: coordinates of the vertex of the triangle should be of type int or float!\nTry again:')
            else:
                vertexes += new_vertex
    return vertexes


if __name__ == '__main__':
    print('Area of the triangle is: {}'.format(area_of_triangle(read_triangle())))
    # import doctest
    # doctest.testmod()

