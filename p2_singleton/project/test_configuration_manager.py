import unittest
import json
from unittest.mock import patch, mock_open

# Import the ConfigManager class from your module
from configuration_manager import ConfigManager

class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.config_manager = ConfigManager()

    # Mock the open function to simulate file operations
    @patch('builtins.open', new_callable=mock_open)
    def test_load_config(self, mock_file_open):
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

    def test_get_setting(self):
        # Set some configuration data manually
        self.config_manager.config_data = {
            'database.host': 'localhost',
            'api.port': 8080
        }

        # Test getting an existing setting
        db_host = self.config_manager.get_setting('database.host')
        self.assertEqual(db_host, 'localhost')

        # Test getting a non-existing setting
        non_existing_setting = self.config_manager.get_setting('non_existing_setting')
        self.assertIsNone(non_existing_setting)

    @patch('builtins.open', new_callable=mock_open)
    def test_load_non_existent_file(self, mock_file_open):
        # Simulate loading a non-existent file
        mock_file_open.side_effect = FileNotFoundError

        # Call the load_config method with a non-existent file
        self.config_manager.load_config('non_existent_file.json')

        # Assert that config_data is still an empty dictionary
        self.assertEqual(self.config_manager.config_data, {})

    @patch('builtins.open', new_callable=mock_open)
    def test_load_empty_file(self, mock_file_open):
        # Mock an empty JSON file
        mock_file_open.return_value.read.return_value = ''

        # Call the load_config method with an empty file
        self.config_manager.load_config('empty_file.json')

        # Assert that config_data is still an empty dictionary
        self.assertEqual(self.config_manager.config_data, {})

    # Add more test cases for edge cases, negative scenarios, and concurrent access if needed

if __name__ == '__main__':
    unittest.main()
