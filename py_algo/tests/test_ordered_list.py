# import TestCase & random package
from unittest import TestCase
import random
# import module to be tested
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

    def test_add(self):
        """
        A method to test the add method of unordered list
        """
        lst = OrderedList()
        lst.add(15)
        self.assertTrue(lst.head.getData()==15)
        lst.add(17)
        self.assertFalse(lst.head.getData()==17)
        self.assertTrue(lst.head.getData()==15)
        lst.add(12)
        self.assertTrue(lst.head.getData()==12)
        self.assertFalse(lst.head.getData()==15)
        self.assertFalse(lst.head.getData()==17)
        lst.add(9)
        self.assertTrue(lst.head.getData()==9)
        self.assertFalse(lst.head.getData()==12)
        self.assertFalse(lst.head.getData()==15)
        self.assertFalse(lst.head.getData()==17)
        lst.add(13)
        self.assertTrue(lst.head.getData()==9)
        self.assertFalse(lst.head.getData()==12)
        self.assertFalse(lst.head.getData()==13)
        self.assertFalse(lst.head.getData()==15)
        self.assertFalse(lst.head.getData()==17)
        lst.remove(9)
        lst.remove(12)
        self.assertFalse(lst.head.getData()==9)
        self.assertFalse(lst.head.getData()==12)
        self.assertTrue(lst.head.getData()==13)
        self.assertFalse(lst.head.getData()==15)
        self.assertFalse(lst.head.getData()==17)

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


    def test_remove(self):
        """
        A method to test the remove method of ordered list
        """
        lst_items = []
        for i in range(1000):
            number = random.randint(0,10000000)
            while True:
                if number not in lst_items:
                    break
                else:
                    number = random.randint(0,10000000)
            lst_items.append(number)

        lst = OrderedList()

        for item in lst_items:
            lst.add(item)

        random.shuffle(lst_items)

        for item in lst_items:
            self.assertTrue(lst.search(item))
            lst.remove(item)
            self.assertFalse(lst.search(item))
