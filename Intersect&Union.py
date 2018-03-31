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
    res = list(set(args[0]))
    for arg in args:
        temp = res.copy()
        for elem in res:
            if elem not in arg:
                temp.remove(elem)
        res = temp
    return res


print(intersect("dashfkjsahfe", 'abacaba', "fwhahsiuhfdsa"))
#print(union("dashfkjsahfe", 'abacaba', "fwhahsiuhfdsa"))