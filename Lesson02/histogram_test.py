import unittest
from unittest.mock import patch
import Histogram

# filepath: c:\Git\PythonLessons\Lessons\Lesson02\test_Histogram.py

class TestHistogram(unittest.TestCase):
    @patch('builtins.print')
    def test_draw(self, mock_print):
        # Create an instance of Histogram with default character '*'
        histogram = Histogram.clsHistogram()
        histogram.items = [3, 5, 2]  # Set specific items for testing
        
        # Call the draw method
        histogram.draw()
        
        # Verify the printed output
        expected_calls = [
            unittest.mock.call('***'),
            unittest.mock.call('*****'),
            unittest.mock.call('**'),
            unittest.mock.call('---------------------------------')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

        # Test with a different character
        histogram.character = '#'
        histogram.draw()
        
        # Verify the printed output with the new character
        expected_calls = [
            unittest.mock.call('###'),
            unittest.mock.call('#####'),
            unittest.mock.call('##'),
            unittest.mock.call('---------------------------------')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()