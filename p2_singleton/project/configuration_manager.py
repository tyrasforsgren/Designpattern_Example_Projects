"""
ConfigManager Module

This module defines a configuration manager class, 'ConfigManager', that
utilizes the Singleton pattern. It allows loading and accessing configuration
settings from a JSON file.

Classes
-------
ConfigMeta:
    A metaclass that enforces the Singleton pattern by ensuring that only one
    instance of a class can exist at a time.
ConfigManager(ConfigMeta):
    The main configuration manager class that loads and manages configuration
    settings from a JSON file.

Global functions
----------------
None
"""

import json

class ConfigMeta(type):
    """
    Metaclass for enforcing the Singleton pattern.

    This metaclass ensures that only one instance of any class inheriting from it
    can exist.

    Attributes
    ----------
    _instances : dict
        A dictionary to store instances of inheriting classes.

    Methods
    -------
    __call__(cls):
        Override of the default __call__ method to enforce the Singleton pattern.
    """
    _instances = {}

    def __call__(cls):
        """
        Override of the default __call__ method to enforce the Singleton pattern.

        Parameters
        ----------
        cls : type
            The class being instantiated.

        Returns
        -------
        object
            The single instance of the class.
        """
        if cls not in cls._instances:
            # Create a new instance if none exists for the inheriting class
            instance = super().__call__()
            cls._instances[cls] = instance
        return cls._instances[cls]

class ConfigManager(metaclass=ConfigMeta):
    """
    Configuration Manager Class.

    This class loads and manages configuration settings from a JSON file.

    Attributes
    ----------
    config_data : dict
        A dictionary that holds the loaded configuration data.

    Methods
    -------
    load_config(self, filename):
        Load configuration settings from a JSON file.
    get_setting(self, key):
        Get a specific setting from the loaded configuration data.

    """
    def __init__(self):
        """
        Initialize the ConfigManager instance.

        The ConfigManager class stores configuration data and ensures only one
        instance exists.
        """
        self.config_data = {}  # Will hold loaded data

    def load_config(self, filename):
        """
        Load configuration settings from a JSON file.

        Parameters
        ----------
        filename : str
            The path to the JSON configuration file.

        Returns
        -------
        None

        """
        try:
            # Attempt loading JSON and assign it to config_data
            with open(filename, 'r') as config_file:
                self.config_data = json.load(config_file)
        except FileNotFoundError:
            print(f"Config file '{filename}' not found.")

    def get_setting(self, key):
        """
        Get a specific setting from the loaded configuration data.

        Parameters
        ----------
        key : str
            The key to look up in the configuration data.

        Returns
        -------
        object
            The value associated with the key, or None if the key is not found.
        """
        return self.config_data.get(key, None)

if __name__ == '__main__':
    # Create ConfigManager as a demo.
    database_manager = ConfigManager()
    api_manager = ConfigManager()

    # Check if both instances are the same: FIXME: What?????
    print('Database Manager ID:', id(database_manager))
    print('API Manager ID:', id(api_manager))
    print('Instances are same: ', database_manager is api_manager)

    # Load configuration settings from the JSON file.
    database_manager.load_config(r'p2_singleton/docs/config_sample.json')
    api_manager.load_config(r'p2_singleton/docs/config_sample.json')


    # Get and print specific settings.
    db_host = database_manager.get_setting('database.host')
    api_port = api_manager.get_setting('api.port')

    print(f"Database Host: {db_host}")
    print(f"API Port: {api_port}")
