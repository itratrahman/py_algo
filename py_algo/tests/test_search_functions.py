# import unittest TestCase
from unittest import TestCase
# import random package
import random
# import search from py_algo
from py_algo.search import search

class TestSequetialSearch(TestCase):
    """
    Test class for sequential search methods
    """
    def test_import(self):
        """
        Test imports of different type of search methods
        """
        try:
            from py_algo.search import _sequential_search
        except:
            raise Exception("Could not import _sequential_search")

    def test_sequential_search(self):
        """
        Method to test sequential search
        """
        for i in range(100):
            list_of_items = []
            for j in range(10):
                num = random.randint(0,100000000)
                if num not in list_of_items:
                    list_of_items.append(num)
            for num in list_of_items:
                self.assertTrue(search(list_of_items, num, method = "sequential"))
            for k in range(10):
                num = random.randint(0,100000000)
                if num not in list_of_items:
                    self.assertFalse(search(list_of_items, num, method = "sequential"))


class TestBinarySearch(TestCase):
    """
    Test class for binary search methods
    """
    def test_import(self):
        """
        Test imports of different type of search methods
        """
        try:
            from py_algo.search import _binary_search_iterative
        except:
            raise Exception("Could not import _binary_search_iterative")
        try:
            from py_algo.search import _binary_search_recursive
        except:
            raise Exception("Could not import _binary_search_recursive")

    def test_binary_search_iterative(self):
        """
        Method to test binary search(iterative)
        """
        for i in range(100):
            list_of_items = []
            for j in range(100):
                num = random.randint(0,100000000)
                if num not in list_of_items:
                    list_of_items.append(num)
            list_of_items.sort()
            for num in list_of_items:
                self.assertTrue(search(list_of_items, num, method = "binary"))
            for k in range(100):
                num = random.randint(0,100000000)
                if num not in list_of_items:
                    self.assertFalse(search(list_of_items, num, method = "binary"))

        for i in range(100):
            list_of_items = []
            for j in range(100):
                num = random.randint(0,100000000)
                if num not in list_of_items:
                    list_of_items.append(num)
            list_of_items.sort()
            for num in list_of_items:
                self.assertTrue(search(list_of_items, num, method = "binary_iterative"))
            for k in range(100):
                num = random.randint(0,100000000)
                if num not in list_of_items:
                    self.assertFalse(search(list_of_items, num, method = "binary_iterative"))

    def test_binary_search_recursive(self):
        """
        Method to test binary search(recursive)
        """
        for i in range(100):
            list_of_items = []
            for j in range(100):
                num = random.randint(0,100000000)
                if num not in list_of_items:
                    list_of_items.append(num)
            list_of_items.sort()
            for num in list_of_items:
                self.assertTrue(search(list_of_items, num, method = "binary_recursive"))
            for k in range(100):
                num = random.randint(0,100000000)
                if num not in list_of_items:
                    self.assertFalse(search(list_of_items, num, method = "binary_recursive"))

        for i in range(100):
            list_of_items = []
            for j in range(100):
                num = random.randint(0,100000000)
                if num not in list_of_items:
                    list_of_items.append(num)
            list_of_items.sort()
            for num in list_of_items:
                self.assertTrue(search(list_of_items, num))
            for k in range(100):
                num = random.randint(0,100000000)
                if num not in list_of_items:
                    self.assertFalse(search(list_of_items, num))
