
class Deque(object):

    '''
    Class implementation of Deque data structure
    '''

    def __init__(self):
        '''
        Class constructor which initializes the Deque
        '''
        self.items = []

    def isEmpty(self):

        '''
        Class method to check whether the Queue is empty
        '''
        return self.items == []

    def addFront(self, item):
        '''
        Class method to add item to the front of the Deque
        '''
        pass

    def addRear(self, item):
        '''
        Class method to add item to the rear of the Deque
        '''
        pass

    def removeFront(self):
        '''
        Class method to remove item from front of the Deque
        '''
        pass

    def removeRear(self):
        '''
        Class method to remove item from the rear of the Deque
        '''
        pass

    def size(self):
        '''
        Class method to return the size of Queue
        '''
        return len(self.items)
