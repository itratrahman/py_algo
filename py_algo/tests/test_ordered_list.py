from unittest import TestCase
import random
from py_algo.data_struct import OrderedList


class TestOrderedList(TestCase):
    """
    Test class for testing unordered list
    """

    def test_constructor(self):
        """
        A method to test the constructor of unordered list
        """
        lst = OrderedList()
        self.assertTrue(lst.isEmpty)
        self.assertTrue(lst.head is None)

    def test_size(self):
        """
        A method to test the size method of unordered list
        """
        for i in range(100):
            lst = OrderedList()
            counter = 0
            length = random.randint(0,1000)
            for j in range(length):
                number = random.randint(0,1000)
                lst.add(number)
            self.assertTrue(lst.size() == length)

    
