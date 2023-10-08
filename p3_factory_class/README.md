# Vehicle Factory Script

This script demonstrates the use of a Vehicle Factory to create different types of vehicles (Car, Motorcycle, Bicycle) based on parameters. It defines a set of vehicle classes and a factory class for creating instances of these
classes.

## Installation

To use this module, you need to have Python 3.10.8 installed on your system.

Clone the repository to your computer or download as a .zip file:

> git clone https://github.com/tyrasforsgren/effective_exam_2.git


## Class types

### VehicleType(Enum) : Enumeration class

An enumeration of vehicle types.

- `CAR`: Represents a car.
- `BICYCLE`: Represents a bicycle.
- `MOTORCYCLE`: Represents a motorcycle.

### Vehicle(ABC) : Abstract class

This abstract class defines a contract for vehicle classes, requiring them
to implement the 'get_name' method.

- `get_name(self)`: Abstract method to get the name of the vehicle.

### Concrete Classes : Concrete classes

##### Concrete Car class.
##### Concrete Bicycle class.
##### Concrete Motorbike class.

These classes represent concrete vehicles and implements the 'get_name' method
to return the vehicle name (ex: 'Car'). Inherits from the abstract class Vehicle.

### VehicleFactory : Factory class

This class creates different types of vehicles based on the inputof the user.

## Main Function : Demo

#### main()

Main function for demonstrating the VehicleFactory.

This function creates a VehicleFactory instance and uses it to create different types of vehicles. It prints the names of the created vehicles.

## Usage

Main usage as a study demo. Run this script as an example of Factory Design.

## Issues

Modifications to the VehicleType and VehicleFactory classes are needed to add more
vehicle concrete classes, currently.
FIXME: Make these classes adhere to the Open/Closed Principle (OCP) from SOLID.
