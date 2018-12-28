
class Stack(object):
    """
    Class implementation of Stack data structure
    """
    def __init__(self):
        """
        class constructor which initialized the stack
        """
        self.items = []

    def isEmpty(self):
        """
        a method to check if the stack is empty
        """
        return self.items == []

    def push(self, item):
        """
        a method to push item to the top of the stack
        """
        self.items.append(item)

    def pop(self):
        """
        a method to pop item from the top of the stack
        """
        return self.items.pop()

    def peek(self):
        """
        a method to return the top item of the stack
        """
        return self.items[len(self.items)-1]

    def size(self):
        """
        a method to return the size of the stack
        """
        return len(self.items)
