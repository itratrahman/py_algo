# import TestCase
from unittest import TestCase
# import random package
import random
# import Deque (function that needs to be tested)
from py_algo.data_struct import Deque


class TestDeque(TestCase):
    """
    Test class to test the Deque module
    """

    def test_isEmpty(self):
        """
        A method to test the Deque isEmpty method
        """
        s = Deque()
        self.assertTrue(s.isEmpty())

    def test_len(self):
        """
        A method to test the len method of Deque
        """
        s = Deque()
        self.assertTrue(s.size() == 0)
        self.assertTrue(s.isEmpty())
        s.addRear('bird')
        self.assertTrue(s.size() == 1)
        self.assertFalse(s.isEmpty())
        s.addFront('cat')
        self.assertTrue(s.size() == 2)
        self.assertFalse(s.isEmpty())
        s.addFront("bear")
        self.assertTrue(s.size() == 3)
        self.assertFalse(s.isEmpty())
        s.addRear("snail")
        self.assertTrue(s.size() == 4)
        self.assertFalse(s.isEmpty())
        s.removeRear()
        self.assertTrue(s.size() == 3)
        self.assertFalse(s.isEmpty())
        s.removeFront()
        self.assertTrue(s.size() == 2)
        self.assertFalse(s.isEmpty())
        s.removeRear()
        self.assertTrue(s.size() == 1)
        self.assertFalse(s.isEmpty())
        s.removeFront()
        self.assertTrue(s.size() == 0)
        self.assertTrue(s.isEmpty())

    def test_insert_removal_methods(self):
        """
        A method to test the add and removal methods of Deque
        """
        s = Deque()
        s.addRear("bird")
        s.addFront("cat")
        self.assertTrue(s.removeRear() == "bird")
        s.addRear("bird")
        self.assertTrue(s.removeFront() == "cat")
        s.addFront("cat")
        s.addRear("lizard")
        s.addRear("bear")
        self.assertTrue(s.removeRear() == "bear")
        s.addRear("bear")
        self.assertTrue(s.removeFront() == "cat")
        s.addFront("cat")
        s.addFront("lion")
        s.addFront("tiger")
        self.assertTrue(s.removeFront() == "tiger")
        self.assertTrue(s.removeFront() == "lion")