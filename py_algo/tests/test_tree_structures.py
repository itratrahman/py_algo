# import test case
from unittest import TestCase
# import binary Tree
from py_algo.tree import binary_tree


class TestBinaryTree(TestCase):
    """
    Test class to test methods of binary tree
    """
    def system_test(self):
        """
        System test binary tree
        """
        r = binary_tree('a')
        self.assertTrue(r.get_root_node()=="a")
        self.assertTrue(r.get_left_child()==None)
        r.insert_left('b')
        self.assertTrue(isinstance(r.get_left_child(), (binary_tree)))
        self.assertTrue(r.get_left_child().get_root_node()=="b")
        print(r.get_left_child())
        print(r.get_left_child().get_root_node())
        r.insert_right('c')
        self.assertTrue(isinstance(r.get_right_child(), (binary_tree)))
        self.assertTrue(r.get_right_child().get_root_node()=="c")
        r.get_right_child().set_root_node('hello')
        self.assertTrue(r.get_right_child().get_root_node()=="hello")
