

class Node(object):

    def __init__(self, init_data):
        """
        Class constructor which initializes the initial data of the node,
        and set next reference to None
        """
        self.data = init_data
        self.next = None

    def getData(self):
        """
        A method to return the data in the node
        """
        return self.data

    def getNext(self):
        """
        A method to return the next node of the Node
        """
        return self.next

    def setData(self, new_data):
        """
        A method to set the data of the node
        """
        self.data = new_data

    def setNext(self, new_next):
        """
        A method to set the next node
        """
        self.next = new_next


class UnorderedList(object):

    """
    Class implementation of unordered list
    """
    def __init__(self):
        """
        Constructor which initializes the head of the list to None
        """
        self.head = None

    def isEmpty(self):
        """
        Method to check if the list is empty
        """
        return self.head == None

    def add(self, item):
        """
        Method to add item to the list
        """
        # create the a node with the item as its initial data
        temp = Node(item)
        # point the next reference of the new node
        # to the old first node of the list
        temp.setNext(self.head)
        # point the head of the list to the new node
        self.head = temp

    def size(self):
        """
        Method to compute the size of the list by traversal
        """
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
        """
        Method to search an item in the list
        """
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


    def remove(self,item):
        """
        Method to remove item from list
        """
        # set teh current node to the head
        current_node = self.head
        # set previous node to None
        previous_node = None
        # boolean/indicator variable to indicate whether the search item is found
        found_item = False
        # while the item is not found
        while not found_item:
            # if the current node contains the item to be removed
            # then set found_item to True
            if current_node.getData() == item:
                found_item = True
            # set the previous node to current node
            # and set current node to next node
            else:
                previous_node = current_node
                current_node = current_node.getNext()

        # if previous node points to none
        # then point the head the next node
        # case: when the first item is the item to be removed
        if previous_node == None:
            self.head = current_node.getNext()
        # else set the previous node to the next node of the current Node
        # so that the current node is out of the list
        else:
            previous_node.setNext(current_node.getNext())


class OrderedList(object):

    """
    Class implementation of ordered list
    """

    def __init__(self):
        """
        Class constructor which initializes the head of the list to None
        """
        self.head = None

    def isEmpty(self):
        """
        Method to check if the list is empty
        """
        return self.head == None

    def add(self, item):
        """
        Method to add an item in correct order
        """
        # set teh current node to the head
        current_node = self.head
        # set previous node to None
        previous_node = None
        # boolean/indicator variable to indicate whether
        # current item is greater than the search item,
        # this is initialized to False
        stop = False
        # iterate until current node points to None and stop condiction is not reached
        while current_node is not None and not stop:
            # if the current data is greater them item to be added then stop iterating
            if current_node.getData()>item:
                stop = True
            # else push the current node and previous on node ahead
            else:
                previous_node = current_node
                current_node = current_node.getNext()
        # initializa a node containing the item
        temp = Node(item)
        # if previous node points to none
        # then point the next reference of the new node
        # to the old first node of the list
        if previous_node == None:
            temp.setNext(self.head)
            self.head = temp
        # point the next reference of the new node
        # to the current node of the list
        else:
            temp.setNext(current_node)
            previous_node.setNext(temp)

    def size(self):
        """
        Method to compute the size of the list by traversal
        """
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
        """
        Method to search an item in the list
        """
        # set the current note to the head
        current_node = self.head
        # boolean/indicator variable to indicate whether the search item is found
        found_item = False
        # boolean/indicator variable to indicate whether
        # current item is greater than the search item,
        # this is initialized to False
        stop_search = False
        # while we have not reached the end of node and search item is not found
        while current_node != None and not found_item and not stop_search:
            # if the current node matches the search item
            # then set found_item to True
            if current_node.getData() == item:
                found_item = True
            # else check if the current item is greater than search item
            else:
                # if he current item is greater than search item
                # set stop_search to True
                if current_node.getData()>item:
                    stop_search = True
                # else set the current node to the next node of the current node
                else:
                    current_node = current_node.getNext()
        # return the indicator variable
        return found_item

    def remove(self,item):
        """
        Method to remove item from list
        """
        # set teh current node to the head
        current_node = self.head
        # set previous node to None
        previous_node = None
        # boolean/indicator variable to indicate whether the search item is found
        found_item = False
        # while the item is not found
        while not found_item:
            # if the current node contains the item to be removed
            # then set found_item to True
            if current_node.getData() == item:
                found_item = True
            # set the previous node to current node
            # and set current node to next node
            else:
                previous_node = current_node
                current_node = current_node.getNext()

        # if previous node points to none
        # then point the head the next node
        # case: when the first item is the item to be removed
        if previous_node == None:
            self.head = current_node.getNext()
        # else set the previous node to the next node of the current Node
        # so that the current node is out of the list
        else:
            previous_node.setNext(current_node.getNext())
