#!/usr/bin/env python3.6.4


class Price:
    """This is a descriptor class for some owner class. It checks the value of some attribute of the owner class for
    being more than 0 and less then 100."""

    def __init__(self, label: str):
        """This is a constructor of the class Price. Argument label is the name of the attribute of the owner class
        which value will be protected.

        :param label: Name of the attribute.
        :type label: str.
        """
        self.label = label

    def __get__(self, instance, owner) -> int:
        """This method is called when trying get the value of the label attribute of the owner class, protected by
        this descriptor.

        :param instance: Instance of the owner class.
        :type instance class owner: Class owner, who owns this descriptor.
        :param owner: class.
        :return int: value of the attribute label of the class owner.
        """
        return instance.__dict__[self.label]

    def __set__(self, instance, value: int):
        """This method is called when trying to set the value of the label attribute of the owner class. In this method
        we check if the new value is less the 100 and greater than 0 and raise an exception otherwise.

        :param instance: Instance of the owner class.
        :type instance: class owner
        :param value: int.
        """
        if value > 100 or value < 0:
            raise ValueError('Price must be between 0 and 100!')
        else:
            instance.__dict__[self.label] = value


class Book:
    """Some example class which embodies a book with attributes name, author and price. The attribute price is protected
    by the descriptor class Price."""
    price = Price('price')

    def __init__(self, author: str, name: str, price: int):
        """This is a constructor of class Book.

        :param author: Author of the book.
        :type author: str.
        :param name: Name of the book.
        :type name: str.
        :param price: Price of the book.
        :type price: int.
        """
        self.name = name
        self.author = author
        self.price = price


if __name__ == '__main__':
    b = Book('a', 'b', 10)
    c = Book('a', 'b', 11)
    print(b.price, c.price)
    b.price = 42
    print(c.price)
