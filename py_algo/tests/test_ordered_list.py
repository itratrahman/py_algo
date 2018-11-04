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
