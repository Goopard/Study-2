import time
import functools


def time_counter(func):
    """This is a decorator which counts the time elapsed on the execution of some function and prints the result on the
    screen.

    :param func: Function which will be wrapped by this decorator.
    :type func: function.
    :returns function
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        time_start = time.time()
        temp = func(*args, **kwargs)
        time_finish = time.time()
        res_time = time_finish - time_start
        print('Time elapsed on the execution of the function {}: {}'.format(func.__name__, res_time))
        return temp
    return inner


@time_counter
def foo(a: int):
    """Some function which does a lot of pointless work that takes a lot of time.

    :param a: Some number.
    :type a: int.
    :returns None.
    """
    for i in range(100000000):
        a += 1
    print(a)


foo(1000)
