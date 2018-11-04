from unittest import TestCase
import random
from py_algo.data_struct import OrderedList


class TestOrderedList(TestCase):
    """
    Test class for testing unordered list
    """

    def test_constructor(self):
        """
        A method to test the constructor of ordered list
        """
        lst = OrderedList()
        self.assertTrue(lst.isEmpty)
        self.assertTrue(lst.head is None)

    def test_size(self):
        """
        A method to test the size method of ordered list
        """
        for i in range(100):
            lst = OrderedList()
            counter = 0
            length = random.randint(0,1000)
            for j in range(length):
                number = random.randint(0,1000)
                lst.add(number)
            self.assertTrue(lst.size() == length)


    def test_search(self):
        """
        A method to test the search method of ordered list
        """
        random_numbers = []
        for i in range(10000):
            random_numbers.append(random.randint(0,1000000))

        lst_items = []
        for i in range(100):
            lst_items.append(random.randint(0,1000000))

        lst = OrderedList()

        for item in lst_items:
            lst.add(item)
            self.assertTrue(lst.search(item))

        for item in random_numbers:
            if item not in lst_items:
                self.assertFalse(lst.search(item))
