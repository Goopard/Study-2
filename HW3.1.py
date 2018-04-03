import functools


def fabric(some_lambda):
    def decorator(deco):
        print("Decorator called with argument {}!".format(deco))
        def inner(*dargs, **dkwargs):
            print("Inner called with arguments {}{}!".format(dargs, dkwargs))
            def deeper_inner(func):
                print("Deeper_inner called with argument {}!".format(func))
                def yet_deeper_inner(*args, **kwargs):
                    print("Yet_deeper_inner called with arguments {}{}!".format(args, kwargs))
                    return some_lambda(deco(*dargs, **dkwargs)(func)(*args, **kwargs))
                return yet_deeper_inner
            return deeper_inner
        return inner
    return decorator


@fabric(lambda x: x ** 2)
def ffabric(some_lambda):
    def decorator(deco):
        def inner(func):
            def deeper_inner(*args, **kwargs):
                return some_lambda(deco(func)(*args, **kwargs))
            return deeper_inner
        return inner
    return decorator


#@fabric(lambda x: x ** 2)
def repeat(times: int):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if times:
                temp = func(*args, **kwargs)
            else:
                temp = None
            for i in range(times - 1):
                func(*args, **kwargs)
            return temp
        return inner
    return decorator


@ffabric(lambda x: x ** 2)
def not_very_useful_decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("I'm not useful.")
        return func(*args, **kwargs)
    return inner


@not_very_useful_decorator
def foo(*args, **kwargs):
    print("Foo called!")
    return 3


print(foo(1))
