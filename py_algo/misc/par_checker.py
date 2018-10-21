from ..data_struct import Stack


def par_checker(symbol_string):

    '''
    a function for checking parenthesis

    Arguments:
    symbol_string - string variable which needs to be check of balanced parenthesis

    Returns:
    boolean variable - True if the symbol_string is balanced or else False
    '''
    # stack variable to hold the opening parenthesis
    s = Stack()
    # boolean variable to indicate that the parenthesis are balanced
    # inialize balanced to True
    balanced = True
    # a variable to index the symbol string
    index = 0

    # iterate until end of symbol string is reached
    # and while the symbol string is balanced
    while index < len(symbol_string) and balanced:
        # extract the symbol
        symbol = symbol_string[index]
        # if it is an opening parenthesis then push the symbol to the back of the stack
        if symbol == "(":
            s.push(symbol)
        # else check if it is empty
        else:
            # if it is empty before the end of the symbol string is reached
            # then obviously the symbol string is not balanced
            # so set balanced to False
            if s.isEmpty():
                balanced = False
            # else just pop out the symbol from the back of the stack
            else:
                s.pop()
        # increment the index variable
        index += 1

    # return True if balanced is True and if stack is empty
    if balanced and s.isEmpty():
        return True
    # else return False
    else:
        return False
