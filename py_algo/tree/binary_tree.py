
class binary_tree(object):
    """
    Class module of Binary Tree
    """
    def __init__(self, root_object):
        """
        Class constructor which initializes the root object
        and stores the class fields of left child and right child
        """
        # initialize the root object
        self.key = root_object
        # class fields to hold the left and right child of the subtree
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """
        A method to insert a new node to the subtree
        Arguments:
        new_node - key of the new node that will be
        inserted to left node of the subtree
        """
        # if the node does not have existing left child
        # then just add the new node to the subtree
        if self.left_child == None:
            self.left_child = binary_tree(new_node)
        # insert the new node and push the existing child node
        # down one level in the tree
        else:
            tree = binary_tree(new_node)
            tree.left_child = self.left_child
            self.left_child = tree

    def insert_right(self, new_node):
        """
        A method to insert a new node to the subtree
        Arguments:
        new_node - key of the new node that will be
        inserted to left node of the subtree
        """
        # if the node does not have existing left child
        # then just add the new node to the subtree
        if self.right_child == None:
            self.right_child = binary_tree(new_node)
        # insert the new node and push the existing child node
        # down one level in the tree
        else:
            tree = binary_tree(new_node)
            tree.right_child = self.right_child
            self.right_child = tree

    def get_left_child(self):
        """
        A Method to return the left child of subtree
        """
        return self.left_child

    def get_right_child(self):
        """
        A Method to return the right child of subtree
        """
        return self.right_child

    def set_root_node(self, root_object):
        """
        A Method to the root node of the subtree
        """
        self.key = root_object

    def get_root_node(self):
        """
        A Method to get the root node of the subtree
        """
        return self.key

if __name__ == "__main__":

    r = binary_tree('a')
    print(r.get_root_node())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_root_node())
    r.insert_right('c')
    print(r.get_right_child())
    print(r.get_right_child().get_root_node())
    r.get_right_child().set_root_node('hello')
    print(r.get_right_child().get_root_node())
