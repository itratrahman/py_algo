
def preorder(tree):
    """
    A function which performs preorder traversal of binary tree
    Arguments:
    tree - object of class binary_tree
    """
    # check base case
    if tree:
        # print root node
        print(tree.get_root_node())
        # recursively traverse left child
        preorder(tree.get_left_child())
        # recursively traverse right child
        preorder(tree.get_right_child())

def postorder(tree):
    """
    A function which performs postorder traversal of binary tree
    Arguments:
    tree - object of class binary_tree
    """
    # check the base case
    if tree != None:
        # recursively traverse left child
        postorder(tree.get_left_child())
        # recursively traverse right child
        postorder(tree.get_right_child())
        # print root node
        print(tree.get_root_node())

def inorder(tree):
    """
    A function which performs inorder traversal of binary tree
    Arguments:
    tree - object of class binary_tree
    """
    # check the base case
    if tree != None:
        # recursively traverse left child
        inorder(tree.get_left_child())
        # print root node
        print(tree.get_root_node())
        # recursively traverse right child
        inorder(tree.get_right_child())
