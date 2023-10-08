
"""
Vehicle Factory Script

This script demonstrates the use of a Vehicle Factory to create different types
of vehicles (Car, Motorcycle, Bicycle) based on parameters. It defines
a set of vehicle classes and a factory class for creating instances of these
classes.

Classes
-------
VehicleType(Enum):
    An enumeration of vehicle types Car, Bicycle, and Motorcycle.

Vehicle(ABC):
    An abstract base class (ABC) representing a vehicle with an abstract method
    'get_name' that concrete vehicle classes require.

Car(Vehicle):
    A concrete vehicle class representing a car with a 'get_name' method
    returning the name 'Car'.

Motorcycle(Vehicle):
    A concrete vehicle class representing a motorcycle with a 'get_name' method
    returning the name 'Motorcycle'.

Bicycle(Vehicle):
    A concrete vehicle class representing a bicycle with a 'get_name' method
    returning the name 'Bicycle'.

VehicleFactory:
    A class for creating different types of vehicles based on input parameters.
    It includes a 'create_vehicle' method to instantiate specific vehicle types.

Main Function
-------------
def main():
    Demonstrates the use of the VehicleFactory class to create and print the
    names of different types of vehicles. Also demonstrates an errorcase.

Usage
-----
Run this script as an example of Factory Design.

TODO : Make VehicleType and VehicleFactory adhere to Open/Close from SOLID.
Currently modifications to these classes are needed to be made incase of adding more
vehicle concrete classes.

"""

from abc import ABC, abstractmethod
from enum import Enum, auto


class VehicleType(Enum):
    """
    Enumeration of vehicle types.

    This enumeration defines different types of vehicles, including Car, Bicycle,
    and Motorcycle.

    Attributes
    ----------
    CAR : VehicleType
        Represents a car.
    BICYCLE : VehicleType
        Represents a bicycle.
    MOTORCYCLE : VehicleType
        Represents a motorcycle.

    """
    CAR = auto()
    BICYCLE = auto()
    MOTORCYCLE = auto()

# Create an abstract Vehicle class


class Vehicle(ABC):
    """
    Abstract Vehicle class.

    This abstract class defines a contract for vehicle classes, requiring them
    to implement the 'get_name' method.

    Methods
    -------
    get_name(self)
        Abstract method to get the name of the vehicle.
    """
    @abstractmethod
    def get_name(self):  # Requirement
        """Set requirement for method of same name."""
        pass

# Create concrete vehicle classes (Car, Motorcycle, Bicycle)
# Concrete = inherits from abstract with actual code


class Car(Vehicle):
    """
    Concrete Car class.

    This class represents a concrete car and implements the 'get_name' method
    to return the name 'Car'. Inherits from abstract class Vechicle.
    """

    def get_name(self):
        """Get name of the vehicle
        """
        return "Car"


class Motorcycle(Vehicle):
    """
    Concrete Motorcycle class.

    This class represents a concrete motorcycle and implements the 'get_name'
    method to return the name 'Motorcycle'. Inherits from abstract class Vechicle.
    """

    def get_name(self):
        """Get name of the vehicle
        """
        return "Motorcycle"


class Bicycle(Vehicle):
    """
    Concrete Bicycle class.

    This class represents a concrete bicycle and implements the 'get_name'
    method to return the name 'Bicycle'. Inherits from abstract class Vechicle.
    """

    def get_name(self):
        """Get name of the vehicle
        """
        return "Bicycle"

# Create a VehicleFactory class


class VehicleFactory:
    """
    Vehicle Factory class.

    This class creates different types of vehicles based on the input
    of the user.

    Methods
    -------
    create_vehicle(vehicle_type)
        Create a vehicle instance based on the provided 'vehicle_type'.

    """
    @staticmethod
    def create_vehicle(vehicle_type):
        """
        Create a vehicle instance based on the provided 'vehicle_type'.

        Parameters
        ----------
        vehicle_type : VehicleType
            The type of vehicle to create, specified as a member of the
            VehicleType enumeration.

        Returns
        -------
        Vehicle
            An instance of the specified vehicle type.

        Raises
        ------
        ValueError
            If the provided 'vehicle_type' is invalid.

        """
        if vehicle_type == VehicleType.CAR:
            return Car()
        if vehicle_type == VehicleType.BICYCLE:
            return Bicycle()
        if vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle()
        raise ValueError(
            f'The vehicle type : "{str(vehicle_type)}" is invalid.')

# Example :


def main():
    """
    Main function for demonstrating the VehicleFactory.

    This function creates a VehicleFactory instance and uses it to create
    different types of vehicles. It prints the names of the created vehicles.

    Returns
    -------
    None

    """
    factory = VehicleFactory()

    # Create a Car instance and print its name
    car = factory.create_vehicle(VehicleType.CAR)
    print(f"Vehicle Type: {car.get_name()}")

    # Create a Motorcycle instance and print its name
    motorcycle = factory.create_vehicle(VehicleType.MOTORCYCLE)
    print(f"Vehicle Type: {motorcycle.get_name()}")

    # Attempt to create an invalid vehicle type (should raise an exception)
    try:
        factory.create_vehicle('hj')
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
