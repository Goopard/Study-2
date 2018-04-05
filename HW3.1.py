import functools


def fabric(some_lambda):
    """This is a decorator, which is used to decorate some other decorator deco, which decorates some function.
    Decorator fabric takes lambda some_lambda as an argument, and applies it to the result of the function, which is
    decorated by deco decorator. It is also possible to enable/disable decorator deco, using:
    fabric.off() - to disable the decorator
    fabric.on() - to enable the decorator

    :param some_lambda: Lambda, which will be applied to the function decorated by deco.
    :type some_lambda: function.
    :returns function: Modified decorator deco.
    """
    fabric.decorator_enabled = True

    def decorator_switch_off():
        """This function is used to disable the decorated decorator deco. Does not take any arguments or return
        anything.
        """
        print("Decoration disabled!")
        fabric.decorator_enabled = False

    def decorator_switch_on():
        """This function is used to enable the decorated decorator deco. Does not take any arguments or return
        anything.
        """
        print("Decoration enabled!")
        fabric.decorator_enabled = True

    fabric.off = decorator_switch_off
    fabric.on = decorator_switch_on

    # decorator will be the modified version of our decorated decorator deco.

    def decorator(deco):
        def inner(*dargs, **dkwargs):

            # After this point we have two choices: either the decorated decorator deco takes some arguments, or not. If
            # it does not, than the condition in the lower "if" is true (**dkwargs is empty and the only element of
            # *dargs is the function, which is decorated by deco). And if deco does take arguments (and if it doesn't
            # take only one argument which is function - this case is unsupported by fabric) this condition is false.

            if len(dkwargs) == 0 and len(dargs) == 1 and callable(dargs[0]):

                # Since the decorator deco in this case doesn't take any arguments, we can go on and define the modified
                # version of the decorated function.

                @functools.wraps(dargs[0])
                def deeper_inner(*args, **kwargs):

                    # Before we are ready to try to apply some_lambda for the result of the decorated function, we have
                    # to check if decoration is enabled.

                    if fabric.decorator_enabled:
                        try:
                            return some_lambda(deco(dargs[0])(*args, **kwargs))
                        except TypeError:
                            print("Error! Inapplicable lambda for the function {}!".format(darg[0].__name__))
                    else:
                        try:
                            return some_lambda(dargs[0](*args, **kwargs))
                        except TypeError:
                            print("Error! Inapplicable lambda for the function {}!".format(darg[0].__name__))
                return deeper_inner
            else:

                # In this case the decorator deco did take some arguments, so we first have do define the function,
                # which is returned by the call deco(*dargs, **dkwargs), which will take the decorated function func as
                # an argument.

                def deeper_inner(func):

                    # Here, at last, we can define the function, which will be the modified version of the decorated
                    # function func (with some_lambda applied to its result).

                    @functools.wraps(func)
                    def yet_deeper_inner(*args, **kwargs):

                        # And again we have to check if decoration is enabled.

                        if fabric.decorator_enabled:
                            try:
                                return some_lambda(deco(*dargs, **dkwargs)(func)(*args, **kwargs))
                            except TypeError:
                                print("Error! Inapplicable lambda for the function {}!".format(func.__name__))
                        else:
                            try:
                                return some_lambda(func(*args, **kwargs))
                            except TypeError:
                                print("Error! Inapplicable lambda for the function {}!".format(func.__name__))
                    return yet_deeper_inner
                return deeper_inner
        return inner
    return decorator


@fabric(lambda x: x ** 2)
def repeat(times: int):
    """This is a decorator, which repeats the call of the decorated function for times times, counts the average value
    of the return values, which is returned by the decorated version of the original function.

    :param times: Amount of times the decorated function will be called.
    :type times: int
    :return: function: Modified decorated function.
    """
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if times:
                sum_of_results = func(*args, **kwargs)
            else:
                sum_of_results = None
            for i in range(times - 1):
                sum_of_results += func(*args, **kwargs)
            return sum_of_results / times
        return inner
    return decorator


@fabric(lambda x: x ** 2)
def not_very_useful_decorator(func):
    """This is a useless decorator.

    :param func: The decorated function.
    :type func: function
    :return: function: Modified decorated function.
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("I'm not useful.")
        return func(*args, **kwargs)
    return inner


@repeat(1)
def foo(*args, **kwargs):
    """Some function.

    :param args: Some arguments.
    :param kwargs: More arguments.
    :return: int: The number 3.
    """
    print("Foo called!")
    return 3


fabric.off()
print(foo(1))
fabric.on()
print(foo([1, 2, 3]))
