
class Stack(object):
    """
    Class implementation of Stack data structure
    """
    def __init__(self):
        """
        Class constructor which initializes the stack
        """
        self.items = []

    def isEmpty(self):
        """
        A method to check if the stack is empty
        by comparing it to empty list
        """
        return self.items == []

    def push(self, item):
        """
        A method to push item to the top of the stack,
        We use the list's append method
        """
        self.items.append(item)

    def pop(self):
        """
        A method to pop item from top of the stack
        We use the list's pop method
        """
        return self.items.pop()

    def peek(self):
        """
        A method to return the top item of the stack
        """
        return self.items[len(self.items)-1]

    def size(self):
        """
        A method to return the size of the stack
        """
        return len(self.items)
