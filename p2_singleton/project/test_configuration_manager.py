"""
Test for ConfigManager Module

This script tests the methods of the ConfigManager class from the
configuration_manager module. It focuses on the load_config and get_setting
methods, as well as edge cases. It indirectly tests the accompanied metaclass
ConfigMeta.

Classes
-------
TestConfigManager
    Inherits from unittest.TestCase and contains test methods.

Global functions
----------------
None

"""

import unittest
import json
from unittest.mock import patch, mock_open

# Import the ConfigManager class from your module
from configuration_manager import ConfigManager

class TestConfigManager(unittest.TestCase):
    """
    Test class for ConfigManager.

    This class inherits from unittest.TestCase and contains test methods for the
    ConfigManager class in the configuration_manager module. It focuses on testing
    the load_config and get_setting methods, as well as handling edge cases. This class
    indirectly tests the accompanied metaclass ConfigMeta.

    Attributes
    ----------
    None

    Methods
    -------
    test_load_valid_config_file
        Tests the load_config method with a valid configuration file.
    test_load_non_existent_config_file
        Tests the load_config method with a non-existent configuration file.
    test_load_empty_config_file
        Tests the load_config method with an empty configuration file.
    test_get_existing_setting
        Tests the get_setting method with an existing setting.
    test_get_non_existing_setting
        Tests the get_setting method with a non-existing setting and checks for errors.

    """

    def setUp(self):
        """
        Set up method for creating an instance of ConfigManager.

        This method is called before each test case to create an instance of the
        ConfigManager class, which will be used in the test methods.

        Returns
        -------
        None

        """
        # Set up instance
        self.config_manager = ConfigManager()

    def tearDown(self) -> None:
        """This methods resets the state of the testing evironment
        between thests, thus enuring independance between them.

        Returns
        -------
        None
        
        """
        return super().tearDown()

    def test_load_valid_config_file(self):
        """
        Tests the load_config method with a valid configuration file.

        This method mocks the open function to simulate file operations and then
        calls the load_config method with a valid JSON configuration file.
        It asserts that the config_data has been loaded correctly.

        Returns
        -------
        None

        """
        # Mock the open function to simulate file operations
        with patch('builtins.open', new_callable=mock_open) as mock_file_open:
            # Mock the content of the JSON file
            config_data = {
                'database.host': 'localhost',
                'api.port': 8080
            }
            mock_file_open.return_value.read.return_value = json.dumps(config_data)

            # Call the load_config method
            self.config_manager.load_config('fake_filename.json')

            # Assert that config_data has been loaded correctly
            self.assertEqual(self.config_manager.config_data, config_data)

    def test_load_non_existent_config_file(self):
        """
        Tests the load_config method with a non-existent configuration file.

        This method simulates loading a non-existent file and expects a FileNotFoundError.
        It also checks that the config_data remains an empty dictionary.

        Returns
        -------
        None

        """
        # Simulate loading a non-existent file and expect a FileNotFoundError
        with patch('builtins.open', side_effect=FileNotFoundError):
            # Call the load_config method with a non-existent file
            with self.assertRaises(FileNotFoundError):
                self.config_manager.load_config('non_existent_file.json')

            # Assert that config_data is still an empty dictionary
            self.assertEqual(self.config_manager.config_data, {})

    def test_load_empty_config_file(self):
        """
        Tests the load_config method with an empty configuration file.

        This method mocks an empty JSON file and calls the load_config method
        with the empty file. It checks that config_data remains an empty dictionary.

        Returns
        -------
        None

        """
        # Mock an empty JSON file
        with patch('builtins.open', new_callable=mock_open) as mock_file_open:
            mock_file_open.return_value.read.return_value = '{}'

            # Call the load_config method with an empty file
            self.config_manager.load_config('empty_file.json')

            # Assert that config_data is still an empty dictionary
            self.assertEqual(self.config_manager.config_data, {})

    def test_get_existing_setting(self):
        """
        Tests the get_setting method with an existing setting.

        This method sets up some configuration data manually and then attempts
        to retrieve an existing setting using the get_setting method.
        It checks that the retrieved value matches the expected value.

        Returns
        -------
        None

        """
        # Set some configuration data manually
        self.config_manager.config_data = {
            'database': {
                'host': 'localhost'
            },
            'api': {
                'port': 8080
            }
        }

        # Test getting an existing setting
        db_host = self.config_manager.get_setting(['database', 'host'])
        self.assertEqual(db_host, 'localhost')

    def test_get_non_existing_setting(self):
        """
        Tests the get_setting method with a non-existing setting and checks for errors.

        This method sets up some configuration data manually and then attempts
        to retrieve a non-existing setting using the get_setting method.
        It checks for both KeyError and TypeError exceptions, which can be raised in case of issues.

        Returns
        -------
        None

        """
        # Set some configuration data manually
        self.config_manager.config_data = {
            'database': {
                'host': 'localhost'
            },
            'api': {
                'port': 8080
            }
        }

        # Test getting a non-existing setting and check for both KeyError and TypeError
        with self.assertRaises((KeyError, TypeError)):
            self.config_manager.get_setting(['database', 'user'])

if __name__ == '__main__':
    unittest.main()
