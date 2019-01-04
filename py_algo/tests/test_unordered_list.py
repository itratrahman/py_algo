# import TestCase and random package
from unittest import TestCase
import random
# import module to be tested
from py_algo.data_struct import UnorderedList#

class TestUnorderedList(TestCase):
    """
    Test class for testing unordered list
    """
    def test_constructor(self):
        """
        A method to test the constructor of unordered list
        """
        lst = UnorderedList()
        self.assertTrue(lst.isEmpty)
        self.assertTrue(lst.head is None)

    def test_add(self):
        """
        A method to test the add method of unordered list
        """
        lst = UnorderedList()
        for i in range(100000):
            number = random.randint(0,10000000)
            lst.add(number)
            self.assertTrue(lst.head.getData() == number)
        for i in range(100000):
            lst = UnorderedList()
            number = random.randint(0,10000000)
            lst.add(number)
            self.assertTrue(lst.head.getData() == number)

    def test_size(self):
        """
        A method to test the size method of unordered list
        """
        for i in range(1000):
            lst = UnorderedList()
            counter = 0
            length = random.randint(0,500)
            for j in range(length):
                number = random.randint(0,10000000)
                lst.add(number)
            self.assertTrue(lst.size() == length)

    def test_search(self):
        """
        A method to test the search method of unordered list
        """
        random_numbers = []
        for i in range(10000):
            random_numbers.append(random.randint(0,100000000))

        lst_items = []
        for i in range(100):
            lst_items.append(random.randint(0,100000000))

        lst = UnorderedList()

        for item in lst_items:
            lst.add(item)
            self.assertTrue(lst.search(item))

        for item in random_numbers:
            if item not in lst_items:
                self.assertFalse(lst.search(item))

    def test_remove(self):
        """
        A method to test the remove method of unordered list
        """
        lst_items = []
        for i in range(1000):
            number = random.randint(0,100000000)
            while True:
                if number not in lst_items:
                    break
                else:
                    number = random.randint(0,100000000)
            lst_items.append(number)

        lst = UnorderedList()

        for item in lst_items:
            lst.add(item)

        random.shuffle(lst_items)

        for item in lst_items:
            self.assertTrue(lst.search(item))
            lst.remove(item)
            self.assertFalse(lst.search(item))
