# import test TestCase
from unittest import TestCase
# import binary Tree
from py_algo.graph import Graph, Vertex

class TestGraph(TestCase):
    """
    Test class to test the methods of graph module
    """
    def system_test(self):
        """
        System test the graph module
        """
        g = Graph()
        for i in range(6):
            g.addVertex(i)

        for vert in g.vertList.values():
            self.assertTrue(isinstance(vert, Vertex))
