# pylint: disable=import-error

"""
Test for abstract_electronic_device module

This script tests each method in the abstract_electronic_device module
and the global function.

Classes
-------
TestElectronicDevice
    Inherted of unittest.TestCase containing test methods.

Notes:
Since this is a test class it is assumed that there are no returns.
Additionally there are no parameters because there is no use of
decorators.

"""

import unittest
from unittest.mock import patch
from abstract_electronic_device import Smartphone, \
    Laptop, \
    Smartwatch, \
    display_battery_life


class TestElectronicDevice(unittest.TestCase):
    """
    Test class for abstract_electronic_device module.


    Attributes
    ----------
    None

    Methods
    -------
    test_smartphone_battery_life : None
        asserts the correct return and return type.
    test_laptop_battery_life : None
        asserts the correct return and return type.
    test_smartwatch_battery_life : None
        asserts the correct return and return type.
    test_display_battery_life_success : None
        asserts all Instances are called properly with
        the proper return value.
    test_display_battery_life_raises_error : None
        asserts that error is raised if function is not
        called with a ElectronicDevice instance.

    """

    def test_smartphone_battery_life(self) -> None:
        """This method ensures the output and it's type being correct.
        """
        test_phone = Smartphone()
        output = test_phone.battery_life()
        self.assertIsInstance(output, str)
        # Assert individual str return:
        self.assertEqual(output, "Smartphone battery life: 10 hours.")

    def test_laptop_battery_life(self) -> None:
        """This method ensures the output and it's type being correct.
        """
        test_laptop = Laptop()
        output = test_laptop.battery_life()
        self.assertIsInstance(output, str)
        # Assert individual str return:
        self.assertEqual(output, "Laptop battery life: 5 hours.")

    def test_smartwatch_battery_life(self) -> None:
        """This method ensures the output and it's type being correct.
        """
        test_smartwatch = Smartwatch()
        output = test_smartwatch.battery_life()
        self.assertIsInstance(output, str)
        # Assert individual str return:
        self.assertEqual(output, "Smartwatch battery life: 24 hours.")

    def test_display_battery_life_success(self) -> None:
        """This function prints the output of a method if if is type
        ElectronicDevises, otherwise raises ValueError.
        """
        # Collect all correct outputs in order of instances
        test_devices = [Smartphone(), Laptop(), Smartwatch()]
        outputs = ["Smartphone battery life: 10 hours.",
                   "Laptop battery life: 5 hours.",
                   "Smartwatch battery life: 24 hours."]

        with patch('builtins.print',
                   side_effect=outputs) \
                as mock_print:

            # Compare outputs for each Instance with corresponding outputs
            for index, device in enumerate(test_devices, start=0):
                display_battery_life(device)
                mock_print.assert_called_with(outputs[index])

    def test_display_battery_life_raises_error(self):
        """Test if display_battery_life raises a ValueError with the correct
        message for an invalid device.
        """
        invalid_device = "Not an ElectronicDevice"
        # Assert following func raise an error
        with self.assertRaises(ValueError) as error_occurence:
            display_battery_life(invalid_device)

        # Asserting the correct error message
        self.assertEqual(
            str(error_occurence.exception),  # This is the error message
            'Parameter "device" must be type ElectronicDevice')


if __name__ == '__main__':
    unittest.main()
