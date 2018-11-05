
from unittest import TestCase

from py_algo.data_struct import Queue

class TestQueue(TestCase):
    """
    Test class to test the Queue module
    """
    def test_isEmpty(self):
        """
        A method to test the Queue isEmpty method
        """
        s = Queue()
        self.assertTrue(s.isEmpty())

    def test_enqueue_and_dequeue(self):
        """
        A method to test the Queue enqueue method
        """
        s = Queue()
        s.enqueue("Cat")
        s.enqueue("Parrot")
        s.enqueue("Bird")
        s.enqueue("Apple")
        self.assertTrue(s.dequeue() == "Cat")
        self.assertTrue(s.dequeue() == "Parrot")
        self.assertTrue(s.dequeue() == "Bird")
        self.assertTrue(s.dequeue() == "Apple")

    def test_len(self):
        """
        A method to test the len method of Queue
        """
        s = Queue()
        s.enqueue("Cat")
        self.assertTrue(s.size() == 1)
        s.enqueue("Parrot")
        self.assertTrue(s.size() == 2)
        s.enqueue("Bird")
        self.assertTrue(s.size() == 3)
        s.enqueue("Apple")
        self.assertTrue(s.size() == 4)
