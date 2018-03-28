def union(*args) -> list:
    """This functions creates a union of some strings or lists viewed as sets.

    :param args: Strings or lists that will be united.
    :type args: str or list.
    :returns list -- The required union.
    """
    res = []
    for arg in args:
        for elem in arg:
            if elem not in res:
                res.append(elem)
    return res


def intersect(*args) -> list:
    """This functions creates an intersection of some strings or lists viewed as sets.

    :param args: Strings or lists that will be intersected.
    :type args: str or list.
    :returns list -- The required intersection.
    """
    res = union(*args)
    for elem in res:
        for arg in args:
            if elem not in arg:
                res.remove(elem)
    return res


print(union('abce', ['a', 'b', 'c', 'd']))
print(intersect(['a', 'b', 'c', 'd'], 'abacaba'))
