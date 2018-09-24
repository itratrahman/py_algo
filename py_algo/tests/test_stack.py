
from unittest import TestCase

from py_algo import Stack

class TestStack(TestCase):

    def test_isEmpty(self):
        s = Stack()
        self.assertTrue(s.isEmpty())
