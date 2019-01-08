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
# import module to be tested
from py_algo.data_struct import UnorderedList
# import module to be tested
from py_algo.data_struct import OrderedList


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
            self.assertTrue(lst.head.getData() == 15)
            lst.add(17)
            self.assertFalse(lst.head.getData() == 17)
            self.assertTrue(lst.head.getData() == 15)
            lst.add(12)
            self.assertTrue(lst.head.getData() == 12)
            self.assertFalse(lst.head.getData() == 15)
            self.assertFalse(lst.head.getData() == 17)
            lst.add(9)
            self.assertTrue(lst.head.getData() == 9)
            self.assertFalse(lst.head.getData() == 12)
            self.assertFalse(lst.head.getData() == 15)
            self.assertFalse(lst.head.getData() == 17)
            lst.add(13)
            self.assertTrue(lst.head.getData() == 9)
            self.assertFalse(lst.head.getData() == 12)
            self.assertFalse(lst.head.getData() == 13)
            self.assertFalse(lst.head.getData() == 15)
            self.assertFalse(lst.head.getData() == 17)
            lst.remove(9)
            lst.remove(12)
            self.assertFalse(lst.head.getData() == 9)
            self.assertFalse(lst.head.getData() == 12)
            self.assertTrue(lst.head.getData() == 13)
            self.assertFalse(lst.head.getData() == 15)
            self.assertFalse(lst.head.getData() == 17)

        def test_size(self):
            """
            A method to test the size method of ordered list
            """
            for i in range(100):
                lst = OrderedList()
                counter = 0
                length = random.randint(0, 1000)
                for j in range(length):
                    number = random.randint(0, 1000)
                    lst.add(number)
                self.assertTrue(lst.size() == length)

        def test_search(self):
            """
            A method to test the search method of ordered list
            """
            random_numbers = []
            for i in range(10000):
                random_numbers.append(random.randint(0, 1000000))

            lst_items = []
            for i in range(100):
                lst_items.append(random.randint(0, 1000000))

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
                number = random.randint(0, 10000000)
                while True:
                    if number not in lst_items:
                        break
                    else:
                        number = random.randint(0, 10000000)
                lst_items.append(number)

            lst = OrderedList()

            for item in lst_items:
                lst.add(item)

            random.shuffle(lst_items)

            for item in lst_items:
                self.assertTrue(lst.search(item))
                lst.remove(item)
                self.assertFalse(lst.search(item))
