from unittest import TestCase
from py_algo.misc import infix2postfix, compute_operation

class TestInfixConverter(TestCase):

    '''
    Test class to test the infix converter functions
    '''

    def test_infix2postfix(self):

        '''
        Test method to test infic to postfix converter function
        '''
        self.assertTrue(infix2postfix("A * B + C * D") == 'A B * C D * +')
        self.assertTrue(infix2postfix("( A + B ) * C - ( D - E ) * ( F + G )") == 'A B + C * D E - F G + * -')

    def test_compute_operation(self):

        '''
        Test method to test compute_operation functions
        '''
        self.assertTrue(compute_operation('*', 5, 6) == 30)
        self.assertTrue(compute_operation('+', 5, 6) == 11)
        self.assertTrue(compute_operation('-', 5, 6) == -1)
        self.assertTrue(compute_operation('/', 5, 6) == 5/6)
        self.assertTrue(compute_operation('*', 3, 5) == 15)
        self.assertTrue(compute_operation('+', 3, 5) == 8)
        self.assertTrue(compute_operation('-', 3, 5) == -2)
        self.assertTrue(compute_operation('/', 3, 5) == 3/5)
