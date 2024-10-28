import unittest
from unittest.mock import patch, mock_open, Mock
from src.mock_up import *

class TestOperations(unittest.TestCase):
    
    @patch('builtins.open', new_callable=mock_open, read_data='test data')
    def test_read_data_from_file_success(self, mock_file):
        # Test successful file read
        result = read_data_from_file('test.txt')
        mock_file.assert_called_once_with('test.txt', 'r')
        self.assertEqual(result, 'test data')

    @patch('builtins.open')
    def test_read_data_from_file_not_found(self, mock_file):
        # Test file not found scenario
        mock_file.side_effect = FileNotFoundError()
        with self.assertRaises(FileNotFoundError):
            read_data_from_file('nonexistent.txt')

    @patch('subprocess.run')
    def test_execute_command_success(self, mock_run):
        # Test successful command execution
        mock_result = Mock()
        mock_result.stdout = 'command output'
        mock_run.return_value = mock_result
        
        result = execute_command(['ls', '-l'])
        
        mock_run.assert_called_once_with(['ls', '-l'], capture_output=True, text=True)
        self.assertEqual(result, 'command output')

    @patch('subprocess.run')
    def test_execute_command_error(self, mock_run):
        # Test command execution failure
        mock_run.side_effect = subprocess.CalledProcessError(1, ['invalid_command'])
        
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(['invalid_command'])

    @patch('time.time')
    def test_perform_action_based_on_time_a(self, mock_time):
        # Test when time is less than 10
        mock_time.return_value = 5
        result = perform_action_based_on_time()
        self.assertEqual(result, 'Action A')

    @patch('time.time')
    def test_perform_action_based_on_time_b(self, mock_time):
        # Test when time is greater than or equal to 10
        mock_time.return_value = 15
        result = perform_action_based_on_time()
        self.assertEqual(result, 'Action B')