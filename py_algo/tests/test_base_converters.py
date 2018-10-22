from unittest import TestCase

from py_algo.math import divideBy2

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
