# import TestCase
from unittest import TestCase
# import function to be tested
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
        self.assertFalse(pal_checker("fdfsdfsdf"))
        self.assertFalse(pal_checker("adfosdajfkljas"))
        self.assertFalse(pal_checker("kfjkdfjiaiern"))
        self.assertFalse(pal_checker("kspadoifpowerimvfshgiaj"))
        self.assertFalse(pal_checker("kfjpaijfsadjfopiasfjj"))
        self.assertFalse(pal_checker("djsoifjsdafjiaodfjsao"))
        self.assertTrue(pal_checker("radar"))
        self.assertTrue(pal_checker("toot"))
        self.assertTrue(pal_checker("madam"))
        self.assertTrue(pal_checker("kerek"))
        self.assertTrue(pal_checker("mallam"))
        self.assertTrue(pal_checker("ballab"))
        self.assertTrue(pal_checker("darad"))
