# import unittest TestCase
from unittest import TestCase
# import random package
import random
# import search from py_algo
from py_algo.search import search

class TestSearch(TestCase):
    """
    Test class for search methods
    """
    def test_import(self):
        """
        Test imports of different type of search methods
        """
        try:
            from py_algo.search import _sequential_search
        except:
            raise Exception("Could not import sequential_search")
        try:
            from py_algo.search import _binary_search_iterative
        except:
            raise Exception("Could not import binary_search_iterative")
        try:
            from py_algo.search import _binary_search_iterative
        except:
            raise Exception("Could not import binary_search_iterative")


    def test_sequential_search(self):
        """
        Method to test sequential search
        """
        for i in range(1000):
            list_of_items = []
            for j in range(100):
                num = random.randint(0,10000000000)
                if num in list_of_items:
                    list_of_items.append(num)
            for num in list_of_items:
                self.assertTrue(search(list_of_items, num, method = "sequential"))
            for j in range(100):
                num = random.randint(0,10000000000)
                if num not in list_of_items:
                    self.assertFalse(search(list_of_items, num, method = "sequential"))

    def test_sequential_search(self):
        """
        Method to test binary search
        """
        for i in range(1000):
            list_of_items = []
            for j in range(100):
                num = random.randint(0,10000000000)
                if num in list_of_items:
                    list_of_items.append(num)
            for num in list_of_items:
                self.assertTrue(search(list_of_items, num, method = "binary_search_iterative"))
            for j in range(100):
                num = random.randint(0,10000000000)
                if num not in list_of_items:
                    self.assertFalse(search(list_of_items, num, method = "binary_search_iterative"))
