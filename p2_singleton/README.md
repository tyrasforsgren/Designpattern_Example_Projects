# Singleton Pattern Example - ConfigManager

This is a Python example demonstrating the Singleton design pattern using a ConfigManager class. The Singleton pattern ensures that a class has only one instance and provides a global access to that instance.

In this example, we use a ConfigManager to manage configuration settings loaded from a JSON file.

## Installation

To use this module, you need to have Python 3.10.8 installed on your system.

Clone the repository to your computer or download as a .zip file:

> git clone https://github.com/tyrasforsgren/effective_exam_2.git


## Usage

To create a ConfigManager instance:

Import:
from config_manager import ConfigManager

Create instance:
config_manager = ConfigManager()

Loading Configuration Settings:
You can load configuration settings from a JSON file using the load_config method.
config_manager.load_config('config.json')

Getting Configuration Settings:
Retrieve specific configuration settings using the get_setting method:
config_manager.get_setting('database.host)

## Unit Tests
Unit tests for the ConfigManager class are provided in the test_config_manager.py file. To run the tests run it as a script.
