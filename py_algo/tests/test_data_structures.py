# import TestCase
from unittest import TestCase
# import random package
import random
# import Deque (function that needs to be tested)
from py_algo.data_struct import Deque
# import module to be tested
from py_algo.data_struct import Queue
# import module to be tested
from py_algo.data_struct import Stack
# import module to be tested
from py_algo.data_struct import Node


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


class TestNode(TestCase):
    """
    Test class for testing Node class
    """
    def test_constructor(self):
        """
        A method to test the methods of node class
        """
        for i in range(1000):
            integer = random.randint(0,10000000)
            node = Node(integer)
            self.assertTrue(node.getData() == integer)

    def test_setData_method(self):
        """
        A method to test the getData method
        """
        for i in range(1000):
            integer1 = random.randint(0,100000000)
            node = Node(integer1)
            for i in range(100):
                integer2 = random.randint(0,100000000)
                node.setData(integer2)
                self.assertTrue(node.getData() == integer2)

    def test_setNext_method(self):
        """
        A method to test the setNext method
        """
        for i in range(1000):
            integer1 = random.randint(0,100000000)
            node = Node(integer1)
            self.assertTrue(node.getNext() == None)
            for i in range(100):
                integer2 = random.randint(0,100000000)
                node.setNext(integer2)
                self.assertTrue(node.getNext() == integer2)
