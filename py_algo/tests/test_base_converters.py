from unittest import TestCase

from py_algo.math import divideBy2
from py_algo.math import base_converter

class TestBaseConverters(TestCase):

    '''
    Test class for testing base converters
    '''

    def test_divide_by_2(self):

        '''
        Test method to test the function of divideBy2
        '''
        self.assertTrue(divideBy2(42) == "101010")
        self.assertTrue(divideBy2(300) == "100101100")
        self.assertTrue(divideBy2(255) == "11111111")
        self.assertTrue(divideBy2(53) == "110101")
        self.assertTrue(divideBy2(1777) == "11011110001")
        self.assertTrue(divideBy2(36) == "100100")
        self.assertTrue(divideBy2(1000) == "1111101000")


    def test_divide_by_2(self):

        '''
        Test method to test the function of divideBy2
        '''
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
