# import TestCase
from unittest import TestCase
# import module to be tested
from py_algo.data_struct import Stack

class TestStack(TestCase):
    """
    Test class to test the Stack module
    """
    def test_isEmpty(self):
        """
        A method to test the Stack isEmpty method
        """
        s = Stack()
        self.assertTrue(s.isEmpty())

    def test_peek(self):
        """
        A method to test the Stack peek mehtod
        """
        s = Stack()
        s.push(4)
        s.push('dog')
        self.assertTrue(s.peek() == 'dog')

    def test_pop(self):
        """
        A method to test the Stack pop method
        """
        s = Stack()
        s.push(4)
        s.push('dog')
        s.push(True)
        self.assertTrue(s.pop() == True)
        self.assertTrue(s.pop() == 'dog')
        self.assertTrue(s.pop() == 4)

    def test_size(self):
        """
        A method to test the Stack size method
        """
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
