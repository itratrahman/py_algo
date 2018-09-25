from unittest import TestCase

from py_algo.misc import par_checker

class TestParChecker(TestCase):

    '''test class to test the parenthesis checker function'''

    def test_par_checker(self):
        '''a method to check the function par_checker'''
        self.assertTrue(par_checker('((()))'))
        self.assertTrue(par_checker('(((())))'))
        self.assertFalse(par_checker('((())'))
        self.assertFalse(par_checker('(((()))'))
