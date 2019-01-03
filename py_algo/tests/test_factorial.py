# import unittest TestCase
from unittest import TestCase
# import factorial function from math
from py_algo.math import factorial
# import math and random package
import math
import random

class TestFactorial(TestCase):
    """
    Test class for testing factorial
    """
    def test_factorial(self):
        """
        Test method to test the function of factorial
        """
        for i in range(100):
            integer = random.randint(1,15)
            self.assertTrue(math.factorial(integer), factorial(integer))
