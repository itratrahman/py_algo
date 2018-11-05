from unittest import TestCase

from py_algo.string import pal_checker

class TestPalChecker(TestCase):
    """
    Test class to test the function palchecker
    """
    def test_pal_checker(self):
        """
        A method to check the function pal_checker
        """
        self.assertFalse(pal_checker("lsdkjfskf"))
        self.assertTrue(pal_checker("radar"))
        self.assertTrue(pal_checker("toot"))
        self.assertTrue(pal_checker("madam"))
        self.assertTrue(pal_checker("kerek"))
        self.assertTrue(pal_checker("mallam"))
