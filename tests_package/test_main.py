'''
Here you'll find all tests for my functions and classes.
To run the tests, navigate to your project directory in the terminal and run the test_main.py file:
run: python -m unittest discover -s tests_package
'''
import sys
sys.path.insert(1,'C:\MARLON\Coding\Python\Slot_Machine')
import unittest
from unittest.mock import patch
from main import deposit

class Test_Deposit(unittest.TestCase):
    '''Contains tests for deposit activity'''
    @patch('builtins.input', return_value='200')
    def test_deposit(self, mock_input):
        '''Confirms that depositing is done successfully'''
        self.assertEqual(deposit(), 200)

    @patch('builtins.input', side_effect=['abc', 'fsdv', '2333'])
    def test_invalid(self, mock_input):
        '''Tests for invalid deposit ammount (Anything thats not a digit)'''
        self.assertRaises(ValueError, deposit)


if __name__ == "__main__":
    unittest.main()
