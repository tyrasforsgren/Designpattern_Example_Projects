# pylint: disable=import-error

"""Demonstration of how to use the abstract_electronic_device module.

Steps:
1: Import module
2: define electronic instance
3: run display_battery_life to see battery life

"""
# Step 1: Import module
import project.abstract_electronic_device as electronic


# Step 2: Create electronic device instances

# Create a Smartphone instance
phone = electronic.Smartphone()
# Create a Laptop instance
lap = electronic.Laptop()
# Create a Smartwatch instance
watch = electronic.Smartwatch()

# Step 3: Use the `display_battery_life` function to view battery life

# Display battery life for the Smartphone
electronic.display_battery_life(phone)
# Display battery life for the Laptop
electronic.display_battery_life(lap)
# Display battery life for the Smartwatch
electronic.display_battery_life(watch)

# Example with an invalid device (will raise an error)
error_example = int
# electronic.display_battery_life(error_example)