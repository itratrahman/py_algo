# import TestCase
from unittest import TestCase
# import functions to be tested
from py_algo.string import infix2postfix, compute_operation, postfixEval
# import function to be tested
from py_algo.string import pal_checker

class TestInfixConverter(TestCase):
    """
    Test class to test the infix converter functions
    """
    def test_infix2postfix(self):
        """
        Test method to test infic to postfix converter function
        """
        self.assertTrue(infix2postfix("A * B + C * D") == 'A B * C D * +')
        self.assertTrue(infix2postfix("( A + B ) * C - ( D - E ) * ( F + G )") == 'A B + C * D E - F G + * -')

    def test_compute_operation(self):
        """
        Test method to test compute_operation function
        """
        self.assertTrue(compute_operation('*', 5, 6) == 30)
        self.assertTrue(compute_operation('+', 5, 6) == 11)
        self.assertTrue(compute_operation('-', 5, 6) == -1)
        self.assertTrue(compute_operation('/', 5, 6) == 5/6)
        self.assertTrue(compute_operation('*', 3, 5) == 15)
        self.assertTrue(compute_operation('+', 3, 5) == 8)
        self.assertTrue(compute_operation('-', 3, 5) == -2)
        self.assertTrue(compute_operation('/', 3, 5) == 3/5)

    def test_postfixEval(self):
        """
        Test method to test the postfixEval function
        """
        self.assertTrue(postfixEval('7 8 + 3 2 + /') == 3.0 )

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
