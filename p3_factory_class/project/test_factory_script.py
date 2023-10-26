"""
Factory Script Unit Tests

This module contains unit tests for a factory script that demonstrates
the use of a Vehicle Factory to create different types of vehicles (Car,
Motorcycle, Bicycle) based on parameters. The script defines a set of
vehicle classes and a factory class for creating instances of these classes.

Classes
-------
TestVehicleTypeEnum(unittest.TestCase):
    A test case class for testing the VehicleType enumeration.

TestCar(unittest.TestCase):
    A test case class for testing the Car class.

TestMotorcycle(unittest.TestCase):
    A test case class for testing the Motorcycle class.

TestBicycle(unittest.TestCase):
    A test case class for testing the Bicycle class.

TestVehicleFactory(unittest.TestCase):
    A test case class for testing the VehicleFactory class.

TestVehicleFactoryScript(unittest.TestCase):
    A test case class for testing the main function of the script.

Global functions
----------------
None
"""

import unittest
from unittest.mock import patch
from io import StringIO
from factory_script import VehicleFactory, VehicleType, Car, Motorcycle, Bicycle
from factory_script import main

class TestVehicleTypeEnum(unittest.TestCase):
    """
    TestVehicleTypeEnum Class

    A test case class for testing the VehicleType enumeration.

    Methods
    -------
    test_enum_values(self):
        Test whether the VehicleType enumeration values are instances of VehicleType.
    """
    def test_enum_values(self):
        """Test whether the VehicleType enumeration values are instances of VehicleType."""
        self.assertIsInstance(VehicleType.CAR, VehicleType)
        self.assertIsInstance(VehicleType.BICYCLE, VehicleType)
        self.assertIsInstance(VehicleType.MOTORCYCLE, VehicleType)

class TestCar(unittest.TestCase):
    """
    TestCar Class

    A test case class for testing the Car class.

    Methods
    -------
    test_get_name(self):
        Test the 'get_name' method of the Car class.
    """
    def test_get_name(self):
        """Test the 'get_name' method of the Car class."""
        car = Car()
        self.assertEqual(car.get_name(), "Car")

class TestMotorcycle(unittest.TestCase):
    """
    TestMotorcycle Class

    A test case class for testing the Motorcycle class.

    Methods
    -------
    test_get_name(self):
        Test the 'get_name' method of the Motorcycle class.
    """
    def test_get_name(self):
        """Test the 'get_name' method of the Motorcycle class."""
        motorcycle = Motorcycle()
        self.assertEqual(motorcycle.get_name(), "Motorcycle")

class TestBicycle(unittest.TestCase):
    """
    TestBicycle Class

    A test case class for testing the Bicycle class.

    Methods
    -------
    test_get_name(self):
        Test the 'get_name' method of the Bicycle class.
    """
    def test_get_name(self):
        """Test the 'get_name' method of the Bicycle class."""
        bicycle = Bicycle()
        self.assertEqual(bicycle.get_name(), "Bicycle")

class TestVehicleFactory(unittest.TestCase):
    """
    TestVehicleFactory Class

    A test case class for testing the VehicleFactory class.

    Methods
    -------
    setUp(self):
        Set up the test environment before each test method.
    tearDown(self):
        Clean up the test environment after each test method.
    test_create_car(self):
        Test the 'create_car' method of the VehicleFactory class.
    test_create_motorcycle(self):
        Test the 'create_motorcycle' method of the VehicleFactory class.
    test_create_bicycle(self):
        Test the 'create_bicycle' method of the VehicleFactory class.
    test_create_invalid_vehicle(self):
        Test creating an invalid vehicle type with the VehicleFactory class.
    """
    def setUp(self) -> None:
        """Set up the test environment before each test method."""
        self.factory = VehicleFactory

    def tearDown(self) -> None:
        """Clean up the test environment after each test method."""
        self.factory = None

    def test_create_car(self):
        """Test the 'create_car' method of the VehicleFactory class."""
        car = self.factory.create_vehicle(VehicleType.CAR)
        self.assertIsInstance(car, Car)

    def test_create_motorcycle(self):
        """Test the 'create_motorcycle' method of the VehicleFactory class."""
        motorcycle = self.factory.create_vehicle(VehicleType.MOTORCYCLE)
        self.assertIsInstance(motorcycle, Motorcycle)

    def test_create_bicycle(self):
        """Test the 'create_bicycle' method of the VehicleFactory class."""
        bicycle = self.factory.create_vehicle(VehicleType.BICYCLE)
        self.assertIsInstance(bicycle, Bicycle)

    def test_create_invalid_vehicle(self):
        """Test creating an invalid vehicle type with the VehicleFactory class."""
        with self.assertRaises(ValueError):
            self.factory.create_vehicle('invalid_type')

class TestVehicleFactoryScript(unittest.TestCase):
    """
    TestVehicleFactoryScript Class

    A test case class for testing the main function of the script.

    Methods
    -------
    test_main_output(self):
        Test the output generated by the main function.
    """
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_output(self, mock_stdout):
        """Test the output generated by the main function."""
        main()
        output = mock_stdout.getvalue()
        expected_output = "Vehicle Type: Car\nVehicle Type: Motorcycle\nError: The vehicle type : \"hj\" is invalid.\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
