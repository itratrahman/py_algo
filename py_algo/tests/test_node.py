# import TestCase & random package
from unittest import TestCase
import random
# import module to be tested
from py_algo.data_struct import Node

class TestNode(TestCase):
    """
    Test class for testing Node class
    """
    def test_constructor(self):
        """
        A method to test the methods of node class
        """
        for i in range(1000):
            integer = random.randint(0,1000)
            node = Node(integer)
            self.assertTrue(node.getData() == integer)

    def test_setData_method(self):
        """
        A method to test the getData method
        """
        for i in range(1000):
            integer1 = random.randint(0,1000)
            node = Node(integer1)
            for i in range(100):
                integer2 = random.randint(0,1000)
                node.setData(integer2)
                self.assertTrue(node.getData() == integer2)

    def test_setNext_method(self):
        """
        A method to test the setNext method
        """
        for i in range(1000):
            integer1 = random.randint(0,1000)
            node = Node(integer1)
            self.assertTrue(node.getNext() == None)
            for i in range(100):
                integer2 = random.randint(0,1000)
                node.setNext(integer2)
                self.assertTrue(node.getNext() == integer2)
