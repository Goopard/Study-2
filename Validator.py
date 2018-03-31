import functools


def validate(lower_bound=None, upper_bound=None, size=None):
    """This is a decorator which checks the arguments of the decorated function for not being lower than upper_bound
    (if it is defined), not being higher than upper_bound(if it is defined) and for the amount of them being exactly
    size (if it is defined).

    :param lower_bound: The lowest possible value of the argument.
    :param upper_bound: The highest possible value of the argument.
    :return: function or None: The original function if the arguments are valid and None otherwise.
    """
    def decorator(func):
        @functools.wraps(func)
        def inner(*args):
            for arg in args:
                too_small = True if lower_bound is not None and arg < lower_bound else False
                too_big = True if upper_bound is not None and arg > upper_bound else False
                wrong_size = True if size is not None and len(args) != size else False
                if too_small or too_big or wrong_size:
                    print("Function call is not valid!")
                    return None
            return func(*args)
        return inner
    return decorator


@validate(lower_bound=0, upper_bound=256, size=3)
def set_pixel(*pixel_values):
    """Some function that creates pixels.

    :param pixel_values: List of values of pixels.
    :type pixel_values: int
    :returns None
    """
    print("Pixel with values {} created!".format(pixel_values))


set_pixel(0, 100, 200)
set_pixel(-1, 100, 200)
set_pixel(0, 100, 300)
set_pixel(0, 1, 2, 3, 4)
