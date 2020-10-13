import unittest
from unittest.mock import patch
from fun_with_collections import basic_list_exception as basic_list


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    @patch('fun_with_collections.basic_list.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):                        # pass input
        with self.assertRaises(ValueError):                             # this is familiar
            basic_list.make_list()        # call the function!

    @patch('fun_with_collections.basic_list.get_input', return_value='-4')  # patch function for input
    def test_make_list_below_range(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            basic_list.make_list()

    @patch('fun_with_collections.basic_list.get_input', return_value='61')  # patch function for input
    def test_make_list_above_range(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            basic_list.make_list()


if __name__ == '__main__':
    unittest.main()
