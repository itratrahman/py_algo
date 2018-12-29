# import unittest TestCase
from unittest import TestCase
# import summation function
from py_algo.math import sum_of_list
# import random package
import random

class TestSumOfList(TestCase):
    """
    Test class for testing sum_of_list
    """
    def test_sum_of_list(self):
        """
        Test method to test the method of sum_of_list
        """
        for i in range(500):
            random_list = []
            for j in range(50):
                random_list.append(random.randint(0,1000000))
            self.assertTrue(sum(random_list) == sum_of_list(random_list))
            self.assertTrue(sum(random_list) == sum_of_list(random_list, method = "recursive"))
