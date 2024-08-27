# Design Patterns Demonstration Projects

This repository showcases Python examples of various design patterns. Below are concise descriptions of each project and their associated design patterns.

## 1. Electronic Device Battery Life Module

**Design Pattern:** Encapsulation and Abstraction

**Overview:** This module defines battery lives for different electronic devices such as smartphones, laptops, and smartwatches. It also includes functionality to display the battery life of these devices.

**Classes:**
- `Smartphone`: Represents a smartphone with a predefined battery life.
- `Laptop`: Represents a laptop with a predefined battery life.
- `Smartwatch`: Represents a smartwatch with a predefined battery life.

---

## 2. Singleton Pattern Example - ConfigManager

**Design Pattern:** Singleton

**Overview:** Demonstrates the Singleton pattern, ensuring that the `ConfigManager` class has only one instance throughout the application. This class manages configuration settings loaded from a JSON file and provides global access to the instance.

**Classes:**
- `ConfigManager`: Manages configuration settings and ensures a single instance across the application.

---

## 3. Vehicle Factory Script

**Design Pattern:** Factory

**Overview:** Illustrates the Factory pattern for creating various types of vehicles (Car, Motorcycle, Bicycle) based on user input. The `VehicleFactory` class creates instances of different vehicle types, demonstrating how to use a factory to manage object creation.

**Classes:**
- `VehicleType` (Enum): Represents different vehicle types.
- `Vehicle` (Abstract Class): Defines a contract for vehicle classes with an abstract method `get_name`.
- `Car`, `Bicycle`, `Motorcycle` (Concrete Classes): Implement the `get_name` method to provide specific vehicle names.
- `VehicleFactory`: Creates instances of vehicles based on user input.

---

## 4. Temperature Sensor Adapter Script

**Design Pattern:** Adapter

**Overview:** Applies the Adapter pattern to enable collaboration between two different temperature sensor classes. The `TemperatureSensorAdapter` class allows a `FahrenheitTemperatureSensor` to be used as if it were a `CelsiusTemperatureSensor`, demonstrating how to adapt incompatible interfaces.

**Classes:**
- `CelsiusTemperatureSensor`: Provides temperature readings in Celsius.
- `FahrenheitTemperatureSensor`: Provides temperature readings in Fahrenheit.
- `TemperatureSensorAdapter`: Adapts the Fahrenheit sensor to be compatible with the Celsius sensor interface.
