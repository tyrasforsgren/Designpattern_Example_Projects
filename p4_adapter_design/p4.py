class CelsiusTemperatureSensor:
    def __init__(self):
        self._temperature = 25

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_celsius(self):
        return self._temperature

class FahrenheitTemperatureSensor:
    def __init__(self):
        self._temperature = 77

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_fahrenheit(self):
        return self._temperature

# TODO: Complete the TemperatureSensorAdapter class
class TemperatureSensorAdapter:
    def __init__(self, sensor):
        self._sensor = sensor

    def set_temperature(self, temperature):
        fahrenheit_temperature = round((temperature * 1.8) + 32,2)
        self._sensor.set_temperature(fahrenheit_temperature)

    def get_temperature_celsius(self):
        return round(((self._sensor._temperature - 32) / 1.8),2)

def display_temperature(sensor):
    print(f"Temperature: {sensor.get_temperature_celsius():.2f} °C")

def test_temperature_sensor_adapter(adapter, celsius_sensor, fahrenheit_sensor):
    
    # Conversion to Farenheit:
    adapter.set_temperature(100) # will se the temp to 100 cs
    fahrenheit_sensor.set_temperature(100) # set the temp to 100 f
    
    # The expected celcius value for farenheit 100:
    # °C = (100°F - 32) × 5/9
    # °C ≈ 37.78 (rounded to two decimals)
    expected_conversion_value = 37.78

    # difference between the converted value and the expected value:
    # We want it to be low
    difference = abs(adapter.get_temperature_celsius() - expected_conversion_value)

    # Is the difference low enough to be ok?
    assert difference < 0.0001, "Adapter conversion is incorrect"

    # Tests double conversion
    celsius_sensor.set_temperature(0) # Celcius set to 0
    adapter.set_temperature(32) # Fist conv: 32c to f

    print('ad_temp_f',adapter._sensor._temperature) # correct
    # Expected f for 32 c: 
    # °F = (32 × 9/5) + 32
    # °F = 89.6
    expected_farenheit = 89.6 # right value for adapter.set_temperature(32)
    
    # Difference between celcius (currently=0) and
    # the celcius to f then back to c
    print('celc',celsius_sensor.get_temperature_celsius()) # ->0
    print('second conv',adapter.get_temperature_celsius()) # ->32
    
    
    difference = abs(celsius_sensor.get_temperature_celsius() - adapter.get_temperature_celsius())

    print('dif,',difference)
    assert difference < 0.0001, "Adapter conversion is incorrect"

    print("All tests passed!")


if __name__ == "__main__":
    celsius_sensor = CelsiusTemperatureSensor() # Default temp = 25
    fahrenheit_sensor = FahrenheitTemperatureSensor() # Default temp = 77
    
    far_adapter = TemperatureSensorAdapter(fahrenheit_sensor) # Use adapter to convert

    display_temperature(celsius_sensor)
    display_temperature(far_adapter)

    # default far 77 converts to 25 celcius, meaning if the conversion
    # works properly, both of the outputs should be 25celcius

    test_temperature_sensor_adapter(far_adapter, celsius_sensor, fahrenheit_sensor)

    # TODO: Uncomment the test function call after implementing the adapter
    # test_temperature_sensor_adapter(adapter, celsius_sensor, fahrenheit_sensor)
