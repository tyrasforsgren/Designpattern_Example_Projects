# Temperature Sensor Adapter Script

This script demonstrates the Adapter Design Pattern to make two incompatible temperature sensor classes work together. It includes classes for CelsiusTemperatureSensor, FahrenheitTemperatureSensor, and TemperatureSensorAdapter.

## Overview

The script implements the Adapter Design Pattern, enabling the collaboration between two different temperature sensor classes - CelsiusTemperatureSensor and FahrenheitTemperatureSensor. It provides a way to display temperatures in Celsius and tests the accuracy of the conversion.

## Installation

To use this script, you need to have Python 3.10.8 installed on your system.

Clone the repository to your computer or download as a .zip file:

> git clone https://github.com/tyrasforsgren/effective_exam_2.git

## Classes

### CelsiusTemperatureSensor

A class representing a temperature sensor providing readings in Celsius.

- `__init__(self)`: Initializes the sensor with a default temperature of 25°C.
- `set_temperature(self, temperature)`: Sets the temperature of the sensor to the given value.
- `get_temperature_celsius(self)`: Retrieves the current temperature reading in Celsius.

### FahrenheitTemperatureSensor

A class representing a temperature sensor providing readings in Fahrenheit.

- `__init__(self)`: Initializes the sensor with a default temperature of 77°F.
- `set_temperature(self, temperature)`: Sets the temperature of the sensor to the given value in Fahrenheit.
- `get_temperature_fahrenheit(self)`: Retrieves the current temperature reading in Fahrenheit.

### TemperatureSensorAdapter

A class that adapts the interface of FahrenheitTemperatureSensor to be compatible with CelsiusTemperatureSensor.

- `__init__(self, sensor)`: Initializes the adapter with a reference to a FahrenheitTemperatureSensor.
- `set_temperature(self, temperature)`: Sets the temperature of the adapter, converting the given value from Celsius to Fahrenheit.
- `get_temperature_celsius(self)`: Retrieves the current temperature reading in Celsius, converting it from Fahrenheit.

## Functions

### display_temperature(sensor)

Displays the temperature in Celsius for a given sensor.

- `sensor`: The sensor object to display the temperature for.

### test_temperature_sensor_adapter(adapter, celsius_sensor, fahrenheit_sensor)

Tests the TemperatureSensorAdapter class for conversion accuracy.

- `adapter`: The TemperatureSensorAdapter instance to test.
- `celsius_sensor`: An instance of CelsiusTemperatureSensor for comparison.
- `fahrenheit_sensor`: An instance of FahrenheitTemperatureSensor for comparison.

## Usage

Run this script to demonstrate the Adapter Design Pattern for temperature sensors.
