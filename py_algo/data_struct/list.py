

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


class UnorderedList(object):

    '''
    Class implementation of unordered list
    '''
    def __init__(self):
        '''
        Constructor which initializes the head of the list to None
        '''
        self.head = None


    def isEmpty(self):
        '''
        Method to check if the list is empty
        '''
        return self.head == None


    def add(self, item):
        '''
        Method to add item to the list
        '''
        # create the a node with the item as its initial data
        temp = Node(item)
        # point the next reference of the new node
        # to the old first node of the list
        temp.setNext(self.head)
        # point the head of the list to the new node
        self.head = temp


    def size(self):
        '''
        Method to compute the size of the list by traversal
        '''
        # set the current note to the head
        current_node = self.head
        # intialize the counter variable to 0
        counter = 0
        # while the current node does not point to None
        while current_node != None:
            # increment the counter variable
            counter += 1
            # initalize the current node to the next node of the current node
            current_node = current_node.getNext()
        # return the size of the list
        return counter


    def search(self,item):
        '''
        Method to search an item in the list
        '''
        # set the current note to the head
        current_node = self.head
        # boolean/indicator variable to indicate whether the search item is found
        found_item = False
        # while we have not reached the end of node and search item is not found
        while current_node != None and not found_item:
            # if the current node matches the search item
            # then set found_item to True
            if current_node.getData() == item:
                found_item = True
            # else set the current node to the next node of the current node
            else:
                current_node = current_node.getNext()
        # return the indicator variable
        return found_item
