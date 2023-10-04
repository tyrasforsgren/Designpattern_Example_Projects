
"""
abstract_electronic_device module

This module defines battery lives of different types of Electronic
devices and provides function for displaying them. The design of
the module is based on OOP stratergy using abstract classes and
methods, imported by abc module (Abstrac Base Class)

Classes
-------
ElectronicDevices : abstract class
    This class defines a common template of requrements for
    inheriting classes defined in this module.
Smartphone:
    This method inherits from abstract class ElectronicDevices
    and provides method returning battery life of a smartphone.
Laptop:
    This method inherits from abstract class ElectronicDevices
    and provides method returning battery life of a laptop.
Smartwatch:
    This method inherits from abstract class ElectronicDevices
    and provides method returning battery life of a smartwatch.

Global functions
----------------
display_battery_life
    This method displays the battery life of an ElectronicDevice
    type instance.

"""

from abc import ABC, abstractmethod

class ElectronicDevice(ABC):
    """
    This class is abstract and defines a template for inheriting classes.

    Methods
    -------
    battery_life : abstract method
        method stating requirement for inheriting classes.

    Inheriting classes
    ------------------
    Smartphone:
        class returning battery life of a smartphone.
    Laptop:
        class returning battery life of a laptop.
    Smartwatch:
        class returning battery life of a smartwatch.

    """

    @abstractmethod # Convert class to abstract
    def battery_life(self): pass # State required method template
        """This abstract method confirms requirement of matching
        method in inheriting classes.

        """

class Smartphone(ElectronicDevice): # Inherit from ElectronicDevice
    """
    Inheriting class of ElectronicDevices containing method returning
    battery life of a smartphone.

    Methods
    -------
    battery_life :
        returns str stating battery life of a smartphone.

    """

    def battery_life(self) -> str:
        """This method returns battery life of a smartphone.

        Parameters
        ----------
        None

        Returns
        -------
        str:
            srt declaring battery life.
        
        Raises
        ------
        None

        """
        return "Smartphone battery life: 10 hours."

class Laptop(ElectronicDevice): # Inherit from ElectronicDevice

    """
    Inheriting class of ElectronicDevices containing method returning
    battery life of a laptop.

    Methods
    -------
    battery_life :
        returns str stating battery life of a laptop.

    """

    def battery_life(self) -> str:
        """This method returns battery life of a laptop.

        Parameters
        ----------
        None

        Returns
        -------
        str:
            srt declaring battery life.
        
        Raises
        ------
        None

        """

        # Set individual battery life
        return "Laptop battery life: 5 hours."

class Smartwatch(ElectronicDevice): # Inherit from ElectronicDevice

    """
    Inheriting class of ElectronicDevices containing method returning
    battery life of a smartwatch.

    Methods
    -------
    battery_life :
        returns str stating battery life of a smartwatch.

    """
    def battery_life(self) -> str:
        """This method returns battery life of a smartwatch.

        Parameters
        ----------
        None

        Returns
        -------
        str:
            srt declaring battery life.
        
        Raises
        ------
        None

        """
        # Set individual battery life
        return "Smartwatch battery life: 24 hours."

def display_battery_life(device:ElectronicDevice):
    """This function prints the battery life of a given ElectronicDevice
    instance and raises roor if wrong type.

    Paramtetrs
    ----------
    device : ElectronicDevice
        Device of which to display info.

    Returns
    -------
    None

    Raises
    ------
    ValueError:
        If parameter is not of ElectronicDevices type.

    Example usage
    -------------
    To display the battery life of a device:
        my_device = Smartphone()
        display_battery_life(my_device)

    """
    try:
        print(device.battery_life())
    except AttributeError:
        raise ValueError('parameter "device" must be type ElectronicDevice')
