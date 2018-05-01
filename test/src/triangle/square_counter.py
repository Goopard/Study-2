def square_of_triangle(vertexes):
    """This function counts the square of a triangle given as a list of 6 numbers - the coordinates of the vertexes.

    Tests:
    Positive ones:
    >>> square_of_triangle([0, 0, 1, 1, 0, 1])
    0.4999999999999998
    >>> square_of_triangle([1, 1, -1, -1, 0, 0])
    0.0
    >>> square_of_triangle([0, 0, 0, 0, 0, 0])
    0.0
    >>> square_of_triangle([1, 1, -1, -1, 1, -1])
    1.9999999999999991

    Negative ones:
    >>> square_of_triangle([0, 0])
    ERROR: 6 coordinates expected, got 2
    >>> square_of_triangle([0, 0, 1, 2, 0, 'a'])
    ERROR: type int or float expected, got <class 'str'>
    >>> square_of_triangle('a')
    ERROR: list of vertexes expected as an argument, got <class 'str'>
    >>> square_of_triangle([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    ERROR: 6 coordinates expected, got 10

    :param vertexes: List of vertexes.
    :type vertexes: list(float or int): List of 6 elements of type int or float - the coordinates of the vertexes.
    :return: float -- Square of the triangle.
    """
    if not isinstance(vertexes, list):
        print('ERROR: list of vertexes expected as an argument, got {}'.format(type(vertexes)))
        return None
    if len(vertexes) != 6:
        print('ERROR: 6 coordinates expected, got {}'.format(len(vertexes)))
        return None
    for coordinate in vertexes:
        if not (isinstance(coordinate, int) or isinstance(coordinate, float)):
            print('ERROR: type int or float expected, got {}'.format(type(coordinate)))
            return None
    a = ((vertexes[0] - vertexes[2]) ** 2 + (vertexes[1] - vertexes[3]) ** 2) ** 0.5
    b = ((vertexes[2] - vertexes[4]) ** 2 + (vertexes[3] - vertexes[5]) ** 2) ** 0.5
    c = ((vertexes[0] - vertexes[4]) ** 2 + (vertexes[1] - vertexes[5]) ** 2) ** 0.5
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def read_triangle():
    """This function reads the vertexes of the triangle.

    :return: list of float -- List of the coordinates of the vertexes of the triangle.
    """
    i = 0
    vertexes = []
    while i < 3:
        new_vertex = input('Please enter the coordinates of the vertex #{}: '.format(i)).split(sep=' ')
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
                i += 1
    return vertexes


if __name__ == '__main__':
    import doctest
    doctest.testmod()
