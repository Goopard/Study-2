#!/usr/bin/env python3

import abc
import functools


class Course:
    """This is a descriptor class for the subclasses of class Currency. It is used to store and operate a course of some
    currency."""

    def __init__(self, value):
        """Constructor of class Course.

        :param value: Value of the course in some conventional units.
        :type value: float or int.
        """
        self.value = value

    def __get__(self, instance, owner):
        """This method is used to access the value of the course. It works in two ways:
        1) When instance is not None this method will return the value of the course:
        >>>e = Euro(10) # Creating an instance of some subclass of the class Currency.
        >>>e.course
        1.22
        2) When instance is None, this method will return a function that takes one argument: some other currency, and
        returns the course of the owner currency to that other currency:
        >>>Euro.course(Dollar)
        1.22

        Note that since the call Some_currency.course (where Some_currency is the subclass of the class Currency)
        returns a function, you can't use it to find out the course of Some_currency. To find out the course use:
        some_instance.course, where some_instance is an instance of Some_currency
        Some_currency(1).course, where you can put any integer or float value instead of 1.

        Also note that you can still use such call to set the value of the course for the currency Some_currency:
        >>>Some_currency.course = 10

        :param instance: Instance of the owner class.
        :type instance: owner.
        :param owner: Class owning this instance of the descriptor Course.
        :type owner: Subclass of the class Currency.
        """
        if instance is not None:
            return self.value
        else:
            def course_to_other(other_currency):
                return self.value / other_currency(1).course
            return course_to_other

    def __set__(self, instance, value):
        """This method is used to set the value of the course.

        :param instance: Instance of some subclass of class Currency
        :type instance: Subclass of the class Currency.
        :param value: New value of the course.
        :type value: float or int.
        :return:
        """
        self.value = value


@functools.total_ordering
class Currency(metaclass=abc.ABCMeta):
    """This is an abstract class which subclasses are used to embody amounts of money of some currencies. Since this
    class is abstract, you are not able to create any instances of class Currency."""

    def __init__(self, value, symbol):
        """Constructor of class currency.

        :param value: Amount of money.
        :type value: float or int.
        :param symbol: Special symbol of the currency, i.eg. $ for dollar.
        :type symbol: str.
        """
        self.value = value
        self.symbol = symbol
        self.currency = type(self).__name__

    def __str__(self):
        """Str representation of some amount of money in some currency."""

        return str(self.value) + ' ' + self.symbol

    def __add__(self, other):
        """This method allows us to sum amounts of money in different (or the same) currencies.

        :param other: Some other instance of some subclass of the class Currency.
        :type other: Subclass of the class Currency.
        """
        self_currency = type(self)
        if isinstance(other, Currency):
            return self_currency(self.value + other.to(self_currency).value)
        else:
            raise TypeError('unable to sum an instance of {} and an instance of {}'.format(self_currency, type(other)))

    def __sub__(self, other):
        """This method allows us to subtract amounts of money in different (or the same) currencies.

        :param other: Some other instance of some subclass of the class Currency.
        :type other: Subclass of the class Currency.
        """
        self_currency = type(self)
        if isinstance(other, Currency):
            return self_currency(self.value - other.to(self_currency).value)
        else:
            raise TypeError('unable to subtract an instance of {} from an instance of class {}'
                            .format(type(other), self_currency))

    def __mul__(self, other):
        """This method allows us to multiply some amount of money in some currency on an int or a float number.

        :param other: Multiplier.
        :type other: float or int.
        """
        self_currency = type(self)
        if isinstance(other, (float, int)):
            return self_currency(self.value * other)
        else:
            raise TypeError('unable to multiply an instance of class {} on an instance of class {}'
                            .format(self_currency.__name__, type(other).__name__))

    def __truediv__(self, other):
        """This method allows us to divide some amount of money in some currency on an int or a float number.

        :param other: Divisor.
        :type other: float or int.
        """
        self_currency = type(self)
        if isinstance(other, (float, int)):
            return self_currency(self.value / other)
        else:
            raise TypeError('unable to divide an instance of class {} on an instance of class {}'
                            .format(self_currency.__name__, type(other).__name__))

    def __eq__(self, other):
        """This method allows us to find out if two amounts of money in different (or the same) currencies are equal.

        :param other: Some other instance of some subclass of the class Currency.
        :type other: Subclass of the class Currency.
        """
        if isinstance(other, Currency):
            return self.value * self.course == other.value * other.course
        else:
            raise TypeError('unable to compare an instance of class {} to an instance of class {}'
                            .format(type(self).__name__, type(other).__name__))

    def __lt__(self, other):
        """This method allows us to find out if one amount of money in some currency is less than the other one.

        :param other: Some other instance of some subclass of the class Currency.
        :type other: Subclass of the class Currency.
        """
        if isinstance(other, Currency):
            return self.value * self.course < other.value * other.course
        else:
            raise TypeError('unable to compare an instance of class {} to an instance of class {}'
                            .format(type(self).__name__, type(other).__name__))

    def to(self, other_currency):
        """This method transforms the instance of some subclass of the class Currency to the other one.

        :param other_currency: The currency we wish to transform this instance to.
        :type other_currency: Subclass of the class Currency.
        :return: other_currency.
        """
        return other_currency(self.value * type(self).course(other_currency))

    @abc.abstractmethod
    def _dummy(self):
        """This is a method that makes this class an abstract one. It is totally useless, but you have to instantiate it
        for all the subclasses of the class Currency."""
        pass


class Dollar(Currency):
    """This class embodies the Dollar currency."""

    course = Course(1)

    def __init__(self, value):
        """Constructor of the class Dollar.

        :param value: Amount of money.
        :type value: float or int.
        """
        super().__init__(value, '$')

    def _dummy(self):
        """The instantiation of the useless method _dummy."""
        pass


class Euro(Currency):
    """This class embodies the Euro currency."""

    course = Course(1.22)

    def __init__(self, value):
        """Constructor of the class Euro.

        :param value: Amount of money.
        :type value: float or int.
        """
        super().__init__(value, '€​')

    def _dummy(self):
        """The instantiation of the useless method _dummy."""
        pass


class Ruble(Currency):
    """This class embodies the Ruble currency."""

    course = Course(1/67)

    def __init__(self, value):
        """Constructor of the class Ruble.

        :param value: Amount of money.
        :type value: float or int.
        """
        super().__init__(value, '₽')

    def _dummy(self):
        """The instantiation of the useless method _dummy."""
        pass


if __name__ == '__main__':
    e = Euro(5)
    print(e.course)
    e.course = 1.5
    c = Euro(10)
    print(c.course)
    d = Dollar(100)
    r = Ruble(1000)
    print(c.to(Dollar))
    print(c + d)
    print(d + c)
    print(Euro.course(Ruble))
    print(e > Euro(6))
    print(e > d)
    print(e == e.to(Ruble))
