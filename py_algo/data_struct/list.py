
class Node(object):

    def __init__(self, init_data):
        '''
        Class constructor which initializes the data
        to initial item pass to the constructor
        and also initializes the next node to none
        '''
        self.data = init_data
        self.next = None

    def getData(self):
        '''
        A method to return the data in the node
        '''
        return self.data

    def getNext(self):
        '''
        A method to return the next node of the Node
        '''
        return self.next

    def setData(self, new_data):
        '''
        A method to set the data of the node
        '''
        self.data = new_data


    def setNext(self, new_next):
        '''
        A method to set the next node
        '''
        self.next = new_next
