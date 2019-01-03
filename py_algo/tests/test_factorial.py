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
        for i in range(200):
            integer = random.randint(1,21)
            self.assertTrue(math.factorial(integer), factorial(integer))

    def test_factorial_recursive(self):
        """
        Test method to test the function of factorial(recursive)
        """
        for i in range(200):
            integer = random.randint(1,21)
            self.assertTrue(math.factorial(integer), factorial(integer, method = "recursive"))

    def test_factorial_iterative(self):
        """
        Test method to test the function of factorial(iterative)
        """
        for i in range(200):
            integer = random.randint(1,21)
            self.assertTrue(math.factorial(integer), factorial(integer, method = "iterative"))
