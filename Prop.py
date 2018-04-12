#!/usr/bin/env python3.6.4

import functools


def prop(attr):
    """This is the decorator version of the descriptor property. It decorates some attribute attr of the owner class."""

    class Inner:
        """This is a class whose object will be the decorated version of the attribute attr."""

        def __init__(self):
            """Constructor of class Inner. It stores the original attr as self.attr and sets attributes set_attr and
            delete_attr to None, since they are not yet initialized."""

            self.attr = attr
            self.set_attr = None
            self.delete_attr = None

        def __get__(self, instance, owner):
            """This method allows us to access the value of property attribute attr of the instance by simply typing:
            >>>instance.attr

            :param instance: Instance of the owner class.
            :type instance: owner.
            :param owner: Class which is the owner of this instance of the class Inner.
            :return: The value of attr(instance).
            """
            return self.attr(instance)

        def __set__(self, instance, value):
            """This method allows us to set the value of attr using special setting method set_attr.

            :param instance: Instance of the owner class.
            :type instance: Some owner class.
            :param value: New value.
            """
            if self.set_attr is not None:
                self.set_attr(instance, value)
            else:
                raise AttributeError("can't set attribute")

        def __delete__(self, instance):
            """This method allows us to delete the attribute attr using special deleting method delete_attr.

            :param instance: Instance of the owner class.
            :type instance: Some owner class.
            """
            if self.delete_attr is not None:
                self.delete_attr(instance)
            else:
                raise AttributeError("can't delete attribute")

        def setter(self, attr_setter):
            """This method is used to initialize the special setting method set_attr. It should be used as a decorator
            for some method attr_setter of the owner class which you want to use a special setting method."""

            self.set_attr = attr_setter

        def deleter(self, attr_deleter):
            """This method is used to initialize the special deleting method delete_attr. It should be used as a decorator
            for some method attr_deleter of the owner class which you want to use a special deleting method."""

            self.delete_attr = attr_deleter

        def __call__(self, *args, **kwargs):
            """This method is here to make the objects of the class Inner callable."""

            return attr(*args, **kwargs)

    return Inner()


class Something:
    def __init__(self, x):
        self.x = x

    @prop
    def attr(self):
        return self.x ** 2

    @attr.setter
    def attr_setter(self, update):
        self.x = update

    @attr.deleter
    def attr_deleter(self):
        del self.x


if __name__ == '__main__':
    s = Something(10)
    print(s.attr)
    s.attr = 3
    print(s.attr)
    s2 = Something(100)
    print(s2.attr)
    print(s.attr)