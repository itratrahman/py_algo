# import unittest TestCase
from unittest import TestCase
# import random package
import random
# import sorting functions
from py_algo.sort import sort_list

class TestSearchMethods(TestCase):
    """
    Test class for testing search methods
    """
    def test_imports(self):
        """
        A method for testing imports
        """
        try:
            from py_algo.sort import sort_list
        except:
            raise Exception("Could not import sort_list")
        try:
            from py_algo.sort import _merge_sort
        except:
            raise Exception("Could not import _merge_sort")
        try:
            from py_algo.sort import _bubble_sort
        except:
            raise Exception("Could not import _bubble_sort")


    def test_grand_search_method(self):
        """
        A method for testing the grand search method
        """
        for i in range(100):
            num_of_elem = random.randint(5,100)
            list_of_items = []
            for j in range(num_of_elem):
                list_of_items.append(random.randint(0,1000))
            self.assertTrue(sort_list(list_of_items) == sorted(list_of_items))

    def test_bubble_sort_method(self):
        """
        A method for testing the bubble search method
        """
        for i in range(100):
            num_of_elem = random.randint(5,100)
            list_of_items = []
            for j in range(num_of_elem):
                list_of_items.append(random.randint(0,1000))
            self.assertTrue(sort_list(list_of_items, method = "bubble") == sorted(list_of_items))

    def test_merge_sort_method(self):
        """
        A method for testing the merge search method
        """
        for i in range(100):
            num_of_elem = random.randint(5,100)
            list_of_items = []
            for j in range(num_of_elem):
                list_of_items.append(random.randint(0,1000))
            self.assertTrue(sort_list(list_of_items, method = "merge") == sorted(list_of_items))
