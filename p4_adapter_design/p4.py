

class CelsiusTemperatureSensor:
    def __init__(self) -> None:
        self._temperature = 25

    def set_temperature(self, temperature) -> None:
        self._temperature = temperature

    def get_temperature_celsius(self) -> int:
        return self._temperature

class FahrenheitTemperatureSensor:
    def __init__(self) -> None:
        self._temperature = 77

    def set_temperature(self, temperature) -> None:
        self._temperature = temperature

    def get_temperature_fahrenheit(self) -> int:
        return self._temperature

class TemperatureSensorAdapter:
    def __init__(self, sensor:FahrenheitTemperatureSensor) -> None:
        self._sensor = sensor

    def set_temperature(self, temperature:int) -> None:
        fahrenheit_temperature = round((temperature * 1.8) + 32,2) # F -> C conversion
        self._sensor.set_temperature(fahrenheit_temperature) # Set as F

    def get_temperature_celsius(self) -> int:
        return round(((self._sensor._temperature - 32) / 1.8),2) # return in C

def display_temperature(sensor) -> None:
    print(f"Temperature: {sensor.get_temperature_celsius():.2f} °C") # 2 decimals

def test_temperature_sensor_adapter(adapter:TemperatureSensorAdapter,
                                    celsius_sensor:CelsiusTemperatureSensor,
                                    fahrenheit_sensor:FahrenheitTemperatureSensor) -> None:
    
    # Conversion to Farenheit:
    adapter.set_temperature(100) # 100 cs
    fahrenheit_sensor.set_temperature(100) # 100 f
    
    # CONVERSION: F -> C
    # F = 100
    # °C = (100°F - 32) × 5/9
    # °C ≈ 37.78 (rounded to two decimals)
    expected_conversion_value = 37.78

    # difference between the converted value and the expected value:
    difference = abs(adapter.get_temperature_celsius() - expected_conversion_value)
    assert difference < 0.0001, "Farenheit to Clecius conversion is incorrect."

    # =====DOUBLE CONVERSION======

    original_c_value = 0 # Celcius
    celsius_sensor.set_temperature(original_c_value)
    adapter.set_temperature(original_c_value)

    # CONVERSION 1: C -> F
    # (C = 0)
    # °F = (0 × 9/5) + 32
    # °F = 32

    # At call adapter.get_temperature_celcius() :
    # CONVERSION 2 : F -> C
    # (F = 31)
    # °C = (32 - 32) × 5/9
    # °C = (0) × 5/9
    # °C = 0
    
    # Difference between Celcius class and Adapter Celcius converion
    difference = (celsius_sensor.get_temperature_celsius() - adapter.get_temperature_celsius()) # 32
    assert difference < 0.0001, "Double adapter conversion is incorrect."

    print("All tests passed!")


if __name__ == "__main__":
    
    celsius_sensor = CelsiusTemperatureSensor() # default 25
    fahrenheit_sensor = FahrenheitTemperatureSensor() # default 77
    far_adapter = TemperatureSensorAdapter(fahrenheit_sensor)

    display_temperature(celsius_sensor) # -> 25
    display_temperature(far_adapter) # -> 77F = 25C
    # They should return the same

    test_temperature_sensor_adapter(adapter=far_adapter,
                                    celsius_sensor=celsius_sensor,
                                    fahrenheit_sensor=fahrenheit_sensor)

