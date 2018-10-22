from ..data_struct import Stack

def divideBy2(number):

    '''
    A function to convert decimal to binary

    Arguments:
    number - a decimal number whose binary is wanted
    Returns:
    binary_string - string containing binary of the number
    '''
    # a stack to store the remainders
    stack_of_remainders = Stack()

    # while the decimal is greater than zero
    while number>0:
        # calculate the remainder when divided by 2
        remainder = number % 2
        # push the remainder to the top of the designated stack
        stack_of_remainders.push(remainder)
        # divide the number by 2 and reinitialize
        number = number//2

    # string to contain the binary representation of the decimal number
    binary_string = ""

    # while the stack of remainders is not empty
    while not stack_of_remainders.isEmpty():
        # pop the remainder from the top of stack and append it to the designated string
        binary_string = binary_string + str(stack_of_remainders.pop())

    # return the binary representation of the decimal number
    return binary_string


def base_converter(number, base):

    '''
    A function to convert decimal to base between 2 and 16

    Arguments:
    number - a decimal number whose base conversion is wanted
    Returns:
    binary_string - string containing base converted representation of the number
    '''
    # digits from 0 to E in base 16
    digits = "0123456789ABCDEF"

    # a stack to store the remainders
    stack_of_remainders = Stack()

    # while the decimal is greater than zero
    while number>0:
        # calculate the remainder when divided by 2
        remainder = number % base
        # push the remainder to the top of the designated stack
        stack_of_remainders.push(remainder)
        # divide the number by 2 and reinitialize
        number = number//base

    # string to contain the binary representation of the decimal number
    binary_string = ""

    # while the stack of remainders is not empty
    while not stack_of_remainders.isEmpty():
        # pop the remainder from the top of stack, find the appropriate digit by index,
        # and append it to the designated string
        binary_string = binary_string + digits[stack_of_remainders.pop()]

    # return the base converted representation of the decimal number
    return binary_string
