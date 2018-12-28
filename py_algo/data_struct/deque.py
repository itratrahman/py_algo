
class Deque(object):
    """
    Class implementation of Deque data structure
    """
    def __init__(self):
        """
        Class constructor which initializes the Deque
        """
        self.items = []

    def isEmpty(self):
        """
        Class method to check whether the Queue is empty
        """
        return self.items == []

    def addFront(self, item):
        """
        Class method to add item to the front of the Deque
        """
        self.items.append(item)

    def addRear(self, item):
        """
        Class method to add item to the rear of the Deque
        """
        self.items.insert(0,item)

    def removeFront(self):
        """
        Class method to remove item from front of the Deque
        """
        return self.items.pop()

    def removeRear(self):
        """
        Class method to remove item from the rear of the Deque
        """
        return self.items.pop(0)

    def size(self):
        """
        Class method to return the size of Queue
        """
        return len(self.items)
