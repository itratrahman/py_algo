# import unittest TestCase
from unittest import TestCase
# import functions to be tested
from py_algo.math import divideBy2
from py_algo.math import base_converter
from py_algo.math import sum_of_list
# import random package
import random


class TestDivideBY2(TestCase):
    """
    Test class for testing divideBy2 method
    """
    def test_divide_by_2(self):
        """
        Test method to test the function of divideBy2
        """
        self.assertTrue(divideBy2(42) == "101010")
        self.assertTrue(divideBy2(300) == "100101100")
        self.assertTrue(divideBy2(255) == "11111111")
        self.assertTrue(divideBy2(53) == "110101")
        self.assertTrue(divideBy2(1777) == "11011110001")
        self.assertTrue(divideBy2(36) == "100100")
        self.assertTrue(divideBy2(1000) == "1111101000")


class TestBaseConverters(TestCase):
    """
    Test class for testing base converters
    """
    def test_base_converter(self):
        """
        Test method to test the grand method of base_converter
        """
        self.assertTrue(base_converter(42,2) == "101010")
        self.assertTrue(base_converter(300,2) == "100101100")
        self.assertTrue(base_converter(255,2) == "11111111")
        self.assertTrue(base_converter(53,2) == "110101")
        self.assertTrue(base_converter(1777,2) == "11011110001")
        self.assertTrue(base_converter(36,2) == "100100")
        self.assertTrue(base_converter(25,2) == "11001")
        self.assertTrue(base_converter(25,16) == "19")
        self.assertTrue(base_converter(512,2) == "1000000000")
        self.assertTrue(base_converter(512,3) == "200222")
        self.assertTrue(base_converter(512,4) == "20000")
        self.assertTrue(base_converter(512,5) == "4022")
        self.assertTrue(base_converter(512,6) == "2212")
        self.assertTrue(base_converter(512,16) == "200")

    def test_base_converter_recursive(self):
        """
        Test method to test the function of base_converter(recursive)
        """
        self.assertTrue(base_converter(42, 2, method="recursive") == "101010")
        self.assertTrue(base_converter(300, 2, method="recursive") == "100101100")
        self.assertTrue(base_converter(255, 2, method="recursive") == "11111111")
        self.assertTrue(base_converter(53, 2, method="recursive") == "110101")
        self.assertTrue(base_converter(1777, 2, method="recursive") == "11011110001")
        self.assertTrue(base_converter(36, 2, method="recursive") == "100100")
        self.assertTrue(base_converter(25, 2, method="recursive") == "11001")
        self.assertTrue(base_converter(25, 16, method="recursive") == "19")
        self.assertTrue(base_converter(512, 2, method="recursive") == "1000000000")
        self.assertTrue(base_converter(512, 3, method="recursive") == "200222")
        self.assertTrue(base_converter(512, 4, method="recursive") == "20000")
        self.assertTrue(base_converter(512, 5, method="recursive") == "4022")
        self.assertTrue(base_converter(512, 6, method="recursive") == "2212")
        self.assertTrue(base_converter(512, 16, method="recursive") == "200")

    def test_base_converter_iterative(self):
        """
        Test method to test the function of base_converter(iterative)
        """
        self.assertTrue(base_converter(42, 2, method="iterative") == "101010")
        self.assertTrue(base_converter(300, 2, method="iterative") == "100101100")
        self.assertTrue(base_converter(255, 2, method="iterative") == "11111111")
        self.assertTrue(base_converter(53, 2, method="iterative") == "110101")
        self.assertTrue(base_converter(1777, 2, method="iterative") == "11011110001")
        self.assertTrue(base_converter(36, 2, method="iterative") == "100100")
        self.assertTrue(base_converter(25, 2, method="iterative") == "11001")
        self.assertTrue(base_converter(25, 16, method="iterative") == "19")
        self.assertTrue(base_converter(512, 2, method="iterative") == "1000000000")
        self.assertTrue(base_converter(512, 3, method="iterative") == "200222")
        self.assertTrue(base_converter(512, 4, method="iterative") == "20000")
        self.assertTrue(base_converter(512, 5, method="iterative") == "4022")
        self.assertTrue(base_converter(512, 6, method="iterative") == "2212")
        self.assertTrue(base_converter(512, 16, method="iterative") == "200")


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