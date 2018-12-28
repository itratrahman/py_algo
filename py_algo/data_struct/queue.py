

class Queue(object):
    """
    Class implementation of Queue data structure
    """
    def __init__(self):
        """
        Class constructor initializes the Queue
        """
        self.items = []

    def isEmpty(self):
        """
        Class method to check whether the Queue is empty
        """
        return self.items == []

    def enqueue(self, item):
        """
        Class method to add a new item to the rear of the queue
        """
        self.items.insert(0,item)

    def dequeue(self):
        """
        Class method to remove the front item from the queue
        """
        return self.items.pop()

    def size(self):
        """
        Class method to return the size of Queue
        """
        return len(self.items)
