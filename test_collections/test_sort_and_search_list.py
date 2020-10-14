import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_list


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_list', returnvalue=5) # input a 5 when prompted
    def test_search_list_found(self, input):
        result = sort_and_search_list.search_list([5, 7, 8])
        self.assertEqual(result, 0)


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_list', returnvalue=5)
    def test_search_list_not_found(self, input):
        result = sort_and_search_list.search_list([6, 7, 8])
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
