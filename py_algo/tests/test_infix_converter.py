from unittest import TestCase
from py_algo.misc import infix2postfix

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
