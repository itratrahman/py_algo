
from unittest import TestCase

from py_algo.data_struct import Stack

class TestStack(TestCase):

    '''test class to test the stack module'''

    def test_isEmpty(self):
        '''test the Stack isEmpty method'''
        s = Stack()
        self.assertTrue(s.isEmpty())

    def test_peek(self):
        '''test the Stack peek mehtod'''
        s = Stack()
        s.push(4)
        s.push('dog')
        self.assertTrue(s.peek() == 'dog')

    def test_pop(self):
        '''test the Stack pop method'''
        s = Stack()
        s.push(4)
        s.push('dog')
        s.push(True)
        self.assertTrue(s.pop() == True)
        self.assertTrue(s.pop() == 'dog')
        self.assertTrue(s.pop() == 4)

    def test_size(self):
        '''test the Stack size method'''
        s = Stack()
        s.push(4)
        s.push('dog')
        s.push(True)
        self.assertTrue(s.size()==3)
        s.pop()
        self.assertTrue(s.size()==2)
        s.pop()
        self.assertTrue(s.size()==1)
        s.pop()
        self.assertTrue(s.size()==0)
        self.assertTrue(s.isEmpty())
