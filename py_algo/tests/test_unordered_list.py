from unittest import TestCase
import random

from py_algo.data_struct import UnorderedList

class TestUnorderedList(TestCase):
    '''
    Test class for testing unordered list
    '''
    def test_constructor(self):
        '''
        A method to test the constructor of unordered list
        '''
        lst = UnorderedList()
        self.assertTrue(lst.isEmpty)
        self.assertTrue(lst.head == None)

    def test_add(self):
        '''
        A method to test the add method of unordered list
        '''
        lst = UnorderedList()
        for i in range(100000):
            number = random.randint(0,1000)
            lst.add(number)
            self.assertTrue(lst.head.getData() == number)
        for i in range(100000):
            lst = UnorderedList()
            number = random.randint(0,1000)
            lst.add(number)
            self.assertTrue(lst.head.getData() == number)
