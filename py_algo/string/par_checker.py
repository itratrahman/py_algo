from ..data_struct import Stack

def simple_par_checker(symbol_string):
    """
    a function for checking parenthesis (does not check for type)
    Arguments:
    symbol_string - string variable which needs to be check of balanced parenthesis
    Returns:
    boolean variable - True if the symbol_string is balanced or else False
    """
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
        # if it is an opening parenthesis then push the symbol to the top of the stack
        if symbol == "(":
            s.push(symbol)
        # else check if it is empty
        else:
            # if it is empty before the end of the symbol string is reached
            # then obviously the symbol string is not balanced
            # so set balanced to False
            if s.isEmpty():
                balanced = False
            # else just pop out the symbol from the top of the stack
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


def match_symbol(open, close):
    """
    A funciton for matching parenthesis symbol type
    Arguments:
    open & close - corresponding opening and closing symbols from a symbol_string
    Returns:
    boolean variable - True if opening and closing symbols match otherwise False
    """
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


def par_checker(symbol_string):
    '''
    A function for checking parenthesis
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
        # if it is an opening parenthesis then push the symbol to the top of the stack
        if symbol in "([{":
            s.push(symbol)
        # else check if it is empty
        else:
            # if it is empty before the end of the symbol string is reached
            # then obviously the symbol string is not balanced
            # so set balanced to False
            if s.isEmpty():
                balanced = False
            # else pop out the symbol from the top of the stack
            # check if opening and closing symbols match type
            else:
                top = s.pop()
                # if the symbol types do no match then set balanced to False
                if not match_symbol(top, symbol):
                    balanced = False
        # increment the index variable
        index += 1

    # return True if balanced is True and if stack is empty
    if balanced and s.isEmpty():
        return True
    # else return False
    else:
        return False
