# Electronic Device Battery Life Module

The Electronic Device Battery Life Module defines battery lives for different types of
electronic devices, such as smartphones, laptops, and smartwatches. It also provides a
function for displaying the battery life of these devices.

## Installation

To use this module, you need to have Python 3.10.8 installed on your system.

Clone the repository to your computer:

>> git clone https://github.com/tyrasforsgren/effective_exam_2.git
   
## Usage
Creating Electronic Device Instances
You can create instances of electronic devices using the following classes:

Smartphone: Represents a smartphone with a predefined battery life.
Laptop: Represents a laptop with a predefined battery life.
Smartwatch: Represents a smartwatch with a predefined battery life.

Example Code

phone = electronic.Smartphone()
lap = electronic.Laptop()
watch = electronic.Smartwatch()

To display the battery life of an electronic device, use the display_battery_life
function and pass the device instance as an argument:

electronic.display_battery_life(phone)
electronic.display_battery_life(lap)
electronic.display_battery_life(watch)

## Handling Errors
If you try to display the battery life of an object that is not an instance of an electronic
device, a ValueError will be raised.

## Testing
This module includes unit tests to ensure the correctness of its functionality. You can run
the tests at test_abstract_electronic_device.py

A demonstration script is also provided in this repository to show how to use the module. You
can run the script at test_abstract_electronic_device.py.
