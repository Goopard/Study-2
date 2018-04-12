#!/usr/bin/env python3.6.4

import abc


class Vehicle(metaclass=abc.ABCMeta):
    """This an abstract class which embodies a vehicle."""

    def __init__(self, year: int, model: str, wheels: int, base_price):
        """Constructor of class Vehicle.

        :param year: Year when the vehicle was assembled.
        :type year: int.
        :param model: Model of the vehicle.
        :type model: str.
        :param wheels: Number of wheels of the vehicle.
        :type wheels: int.
        :param base_price: Base price of the vehicle.
        :type price: float or int.
        """
        self.year = year
        self.model = model
        self.wheels = wheels
        self.base_price = base_price

    @abc.abstractmethod
    def vehicle_type(self):
        """This abstract method prints the type of the vehicle."""
        pass

    def is_motorcycle(self):
        """This method finds out if the vehicle self is motorcycle.

        :return: bool.
        """
        return self.wheels == 2

    def purchase_price(self, distance) -> float:
        """This method counts the price of the vehicle depending on the total travelled distance.

        :param distance: Total travelled distance.
        :type distance: float or int.
        :return: float.
        """
        return self.base_price - 0.1 * distance


class Car(Vehicle):
    """This class embodies a car."""

    def __init__(self, year, model, base_price):
        """Constructor of class Car.

        :param year: Year when the car was assembled.
        :type year: int.
        :param model: Model of the car.
        :type model: str.
        :param base_price: Base price of the car.
        :type price: float or int.
        """
        super().__init__(year, model, 4, base_price)

    def vehicle_type(self):
        """This method prints the type of the vehicle."""
        print('Car')


class Motorcycle(Vehicle):
    """This class embodies a motorcycle."""

    def __init__(self, year, model, base_price):
        """Constructor of class Motorcycle.

        :param year: Year when the motorcycle was assembled.
        :type year: int.
        :param model: Model of the motorcycle.
        :type model: str.
        :param base_price: Base price of the motorcycle.
        :type price: float or int.
        """
        super().__init__(year, model, 2, base_price)

    def vehicle_type(self):
        """This method prints the type of the vehicle."""
        print('Motorcycle')


class Truck(Vehicle):
    """This class embodies a truck."""

    def __init__(self, year, model, base_price):
        """Constructor of class Truck.

        :param year: Year when the truck was assembled.
        :type year: int.
        :param model: Model of the truck.
        :type model: str.
        :param base_price: Base price of the truck.
        :type price: float or int.
        """
        super().__init__(year, model, 6, base_price)

    def vehicle_type(self):
        """This method prints the type of the vehicle."""
        print('Truck')


class Bus(Vehicle):
    """This class embodies a bus."""

    def __init__(self, year, model, base_price):
        """Constructor of class Bus.

        :param year: Year when the bus was assembled.
        :type year: int.
        :param model: Model of the bus.
        :type model: str.
        :param base_price: Base price of the bus.
        :type price: float or int.
        """
        super().__init__(year, model, 8, base_price)

    def vehicle_type(self):
        """This method prints the type of the vehicle."""
        print('Bus')


if __name__ == '__main__':
    c = Car(1999, 'Honda Civic', 200000)
    print(c.purchase_price(130000))
    print(c.is_motorcycle())
    m = Motorcycle(2005, 'Java', 100000)
    print(m.is_motorcycle())
    c.vehicle_type()
