from ..data_struct import Stack

def divideBy2(number):

    '''
    A function to convert decimal to binary

    Arguments:
    number - a number whose binary is wanted
    Returns:
    binary_string - string containing binary of the number
    '''
    # a stack to store the remainders
    stack_of_remainders = Stack()

    while number>0:
        remainder = number % 2
        stack_of_remainders.push(remainder)
        number = number//2

    binary_string = ""

    while not stack_of_remainders.isEmpty():
        binary_string = binary_string + str(stack_of_remainders.pop())

    return binary_string
