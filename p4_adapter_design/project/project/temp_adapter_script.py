
"""
Temperature Sensor Adapter Script

This script implements the Adapter Design Pattern to make two incompatible
temperature sensor classes work together. It includes classes for
CelsiusTemperatureSensor,FahrenheitTemperatureSensor, and
TemperatureSensorAdapter.

Classes
-------
CelsiusTemperatureSensor:
    A class representing a temperature sensor providing readings in Celsius.

FahrenheitTemperatureSensor:
    A class representing a temperature sensor providing readings in Fahrenheit.

TemperatureSensorAdapter:
    A class that adapts the interface of FahrenheitTemperatureSensor to be
    ompatible with CelsiusTemperatureSensor.

Functions
---------
display_temperature(sensor):
    Displays the temperature in Celsius for a given sensor.

test_temperature_sensor_adapter(adapter, celsius_sensor, fahrenheit_sensor):
    Tests the TemperatureSensorAdapter class for conversion accuracy.

Main Function
-------------
if __name__ == "__main__":
    Initializes the temperature sensors, creates an adapter, displays
    temperatures, and runs tests.

Usage
-----
Run this script to demonstrate the Adapter Design Pattern for temperature
sensors.

"""


class CelsiusTemperatureSensor:
    """
    CelsiusTemperatureSensor class.

    A class representing a temperature sensor providing readings in Celsius.

    Methods
    -------
    __init__(self)
        Initializes the CelsiusTemperatureSensor with a default temperature
        of 25°C.

    set_temperature(self, temperature)
        Sets the temperature of the sensor to the given value.

    get_temperature_celsius(self)
        Retrieves the current temperature reading in Celsius.

    """

    def __init__(self) -> None:
        """
        Initialize the CelsiusTemperatureSensor with a default temperature
        of 25°C.
        """
        self._temperature = 25 # C

    def set_temperature(self, temperature:int) -> None:
        """
        Set the temperature of the sensor to the given value.

        Parameters
        ----------
        temperature : int
            The new temperature value in Celsius.

        Returns
        -------
        None

        """
        self._temperature = temperature # C

    def get_temperature_celsius(self) -> int:
        """
        Retrieve the current temperature reading in Celsius.

        Returns
        -------
        int
            The current temperature reading in Celsius.

        """
        return self._temperature # C


class FahrenheitTemperatureSensor:
    """
    FahrenheitTemperatureSensor class.

    A class representing a temperature sensor providing readings in
    Fahrenheit.

    Methods
    -------
    __init__(self)
        Initializes the FahrenheitTemperatureSensor with a default
        temperature of 77°F.

    set_temperature(self, temperature)
        Sets the temperature of the sensor to the given value in Fahrenheit.

    get_temperature_fahrenheit(self)
        Retrieves the current temperature reading in Fahrenheit.

    """

    def __init__(self) -> None:
        """
        Initialize the FahrenheitTemperatureSensor with a default temperature
        of 77°F.
        """
        self._temperature = 77

    def set_temperature(self, temperature:int) -> None:
        """
        Set the temperature of the sensor to the given value in Fahrenheit.

        Parameters
        ----------
        temperature : int
            The new temperature value in Fahrenheit.

        Returns
        -------
        None

        """
        self._temperature = temperature # F

    def get_temperature_fahrenheit(self) -> int:
        """
        Retrieve the current temperature reading in Fahrenheit.

        Returns
        -------
        int
            The current temperature reading in Fahrenheit.

        """
        return self._temperature # F 


class TemperatureSensorAdapter:
    """
    TemperatureSensorAdapter class.

    A class that adapts the interface of FahrenheitTemperatureSensor to be
    compatible with CelsiusTemperatureSensor.

    Methods
    -------
    __init__(self, sensor)
        Initializes the adapter with a reference to a
        FahrenheitTemperatureSensor.

    set_temperature(self, temperature)
        Sets the temperature of the adapter, converting the given value from
        Celsius to Fahrenheit.

    get_temperature_celsius(self)
        Retrieves the current temperature reading in Celsius, converting
        from Fahrenheit.

    """

    def __init__(self, sensor: FahrenheitTemperatureSensor) -> None:
        """
        Initialize the adapter with a reference to a
        FahrenheitTemperatureSensor.

        Parameters
        ----------
        sensor : FahrenheitTemperatureSensor
            An instance of FahrenheitTemperatureSensor to adapt.

        """
        self._sensor = sensor

    def set_temperature(self, temperature: int) -> None:
        """
        Set the temperature of the adapter, converting the given value from
        Celsius to Fahrenheit.

        Parameters
        ----------
        temperature : int
            The new temperature value in Celsius.

        Returns
        -------
        None

        """
        fahrenheit_temperature = round((temperature * 1.8) + 32, 2)
        # Convert Celsius to Fahrenheit
        self._sensor.set_temperature(fahrenheit_temperature) # F
        # Set temperature in Fahrenheit

    def get_temperature_celsius(self) -> int:
        """
        Retrieve the current temperature reading in Celsius, converting
        from Fahrenheit.

        Returns
        -------
        int
            The current temperature reading in Celsius.

        """
        return round(((self._sensor._temperature - 32) / 1.8), 2) # C
        # Return the converted Fahrenheit to Celsius value


def display_temperature(sensor) -> None:
    """
    Display the temperature in Celsius for a given sensor.

    Parameters
    ----------
    sensor : object
        The sensor object to display the temperature for.

    Returns
    -------
    None

    """
    print(f"Temperature: {sensor.get_temperature_celsius():.2f} °C")
    # Display the temperature in Celsius with 2 decimal places


def test_temperature_sensor_adapter(
        adapter:TemperatureSensorAdapter,
        cel_sensor:CelsiusTemperatureSensor,
        far_sensor:FahrenheitTemperatureSensor) -> None:
    """
    Test the TemperatureSensorAdapter class for conversions and accuracy.

    Parameters
    ----------
    adapter : TemperatureSensorAdapter
        The TemperatureSensorAdapter instance to test.

    celsius_sensor : CelsiusTemperatureSensor
        An instance of CelsiusTemperatureSensor for comparison.

    fahrenheit_sensor : FahrenheitTemperatureSensor
        An instance of FahrenheitTemperatureSensor for comparison.

    Returns
    -------
    None

    """
    # Conversion to Fahrenheit:
    adapter.set_temperature(100)  # Set the temperature to 100 Celsius
    far_sensor.set_temperature(100)  # Set the temperature to 100 F

    # Conversion: Fahrenheit to Celsius
    # Fahrenheit = 100
    # °C = (100°F - 32) × 5/9
    # °C ≈ 37.78 (rounded to two decimals)
    expected_conversion_value = 37.78

    # Difference between the converted value and the expected value:
    difference = abs(
        adapter.get_temperature_celsius() -
        expected_conversion_value)
    assert difference < 0.0001, "Fahrenheit to Celsius conversion is incorrect."

    # Double Conversion:

    original_c_value = 0  # Celsius
    cel_sensor.set_temperature(original_c_value)
    adapter.set_temperature(original_c_value)

    # Conversion 1: Celsius to Fahrenheit
    # (Celsius = 0)
    # °F = (0 × 9/5) + 32
    # °F = 32

    # At the call to adapter.get_temperature_celsius():
    # Conversion 2: Fahrenheit to Celsius
    # (Fahrenheit = 32)
    # °C = (32 - 32) × 5/9
    # °C = (0) × 5/9
    # °C = 0

    # Difference between Celsius class and Adapter Celsius conversion
    difference = (cel_sensor.get_temperature_celsius() -
                  adapter.get_temperature_celsius())  # 0
    assert difference < 0.0001, "Double adapter conversion is incorrect."

    print("All tests passed!")


if __name__ == "__main__":
    cel_sensor = CelsiusTemperatureSensor()  # Default 25
    far_sensor = FahrenheitTemperatureSensor()  # Default 77
    far_adapter = TemperatureSensorAdapter(far_sensor)

    display_temperature(cel_sensor)  # -> 25
    display_temperature(far_adapter)  # -> 77°F conv to 25°C
    # They should return the same value 25

    test_temperature_sensor_adapter(adapter=far_adapter,
                                    cel_sensor=cel_sensor,
                                    far_sensor=far_sensor)
