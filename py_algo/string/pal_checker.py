
from ..data_struct import Deque

def pal_checker(string):
    """
    A function to check for pallindrome
    Arguments:
    string - string containing the word which used for pallindrome checking
    Returns:
    equal - a boolean/indicator variable which returns True if string is a pallindrome
    """
    # A deque to store the characters of the string
    deque_of_char = Deque()
    # iterate through each character of the string and store it in the deque
    for char in string:
        deque_of_char.addRear(char)
    # a boolean/indicator variable for pallindrome checking
    equal = True

    #While there is atleast 2 characters left in the string
    while deque_of_char.size()>1 and equal:
        # extract the front and rear elements
        front_elem = deque_of_char.removeFront()
        rear_elem = deque_of_char.removeRear()
        # if the front and rear elements do not match
        # set equal to false
        if front_elem != rear_elem:
            equal = False
    # return the boolean/indicator variable for pallindrome checking
    return equal
