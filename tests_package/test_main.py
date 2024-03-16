'''
Here you'll find all tests for my functions and classes.
To run the tests, navigate to your project directory in the terminal and run the test_main.py file:
run: python -m unittest discover -s tests_package
'''
import sys
sys.path.insert(1,'C:\MARLON\Coding\Python\Slot_Machine\main_package')
import unittest
from unittest.mock import patch
from main_package.main import deposit,get_number_of_lines

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


class Test_Get_Number_Of_Lines(unittest.TestCase):
    '''Contains test for placing a bet activity'''
    
    @patch('builtins.input', side_effect=['1','2','3'])
    def test_valid_input(self, mock_input):
        '''Tests for valid input, value between 1 and 3'''
        self.assertEqual(get_number_of_lines(), 1)
        self.assertEqual(get_number_of_lines(), 2)
        self.assertEqual(get_number_of_lines(), 3)
    
    @patch('builtins.input', side_effect = ["0","Hello", "One","4","0"])
    def test_invalid_input(self, mock_input):
        '''Test for invalid input, anything thats not a digit'''
        with self.assertRaises(ValueError):
            get_number_of_lines()
        


if __name__ == "__main__":
    unittest.main()
