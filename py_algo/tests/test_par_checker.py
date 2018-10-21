from unittest import TestCase

from py_algo.misc import simple_par_checker
from py_algo.misc import match_symbol
from py_algo.misc import par_checker

class TestParChecker(TestCase):

    '''test class to test the parenthesis checker functions'''

    def test_simple_par_checker(self):
        '''a method to check the function simple_par_checker'''
        self.assertTrue(simple_par_checker('((()))'))
        self.assertTrue(simple_par_checker('(((())))'))
        self.assertTrue(simple_par_checker('(()()()())'))
        self.assertTrue(simple_par_checker('(()((())()))'))
        self.assertFalse(simple_par_checker('((())'))
        self.assertFalse(simple_par_checker('(((()))'))
        self.assertFalse(simple_par_checker('()))'))
        self.assertFalse(simple_par_checker('(()()(()'))

    def test_match_symbol(self):
        '''a method to check the function match_symbol'''
        self.assertTrue(match_symbol("{","}"))
        self.assertTrue(match_symbol("(",")"))
        self.assertTrue(match_symbol("[","]"))
        self.assertFalse(match_symbol("{",")"))
        self.assertFalse(match_symbol("{","]"))
        self.assertFalse(match_symbol("(","]"))
        self.assertFalse(match_symbol("(","}"))
        self.assertFalse(match_symbol("[",")"))
        self.assertFalse(match_symbol("[","}"))

    def test_par_checker(self):
        '''a method to check the function par_checker'''
        self.assertTrue(par_checker('((()))'))
        self.assertTrue(par_checker('(((())))'))
        self.assertTrue(par_checker('(()()()())'))
        self.assertTrue(par_checker('(()((())()))'))
        self.assertFalse(par_checker('((())'))
        self.assertFalse(par_checker('(((()))'))
        self.assertFalse(par_checker('()))'))
        self.assertFalse(par_checker('(()()(()'))
        self.assertTrue(par_checker('{{([][])}()}'))
        self.assertTrue(par_checker('[[{{(())}}]]'))
        self.assertTrue(par_checker('[][][](){}'))
        self.assertFalse(par_checker('([)]'))
        self.assertFalse(par_checker('((()]))'))
        self.assertFalse(par_checker('[{()]'))
