

def sum_of_list(list_of_num, method = "iterative"):
    """
    A function which calculate numerical sum of a list of numbers
    Arguments:
    list_of_num - a list containing numbers
    Returns:
    summation - numerical sum of a list of numbers
    """
    # if the method is iterative
    if method == "iterative":
        return _sum_of_list_iterative(list_of_num)
    # if the method is recursive
    elif method == "recursive":
        return _sum_of_list_recursive(list_of_num)
    # else use the iterative method to calculate sum
    else:
        return _sum_of_list_iterative(list_of_num)


def _sum_of_list_iterative(list_of_num):
    """
    A function which calculate numerical sum of a list of numbers
    using iterative method
    Arguments:
    list_of_num - a list containing numbers
    Returns:
    summation - numerical sum of a list of numbers
    """
    # a variable to store the summation, which is initialized to zero
    summation = 0
    # iterate through each number in the list_of_num
    for num in list_of_num:
        summation += num
    # return the summmation
    return summation


def _sum_of_list_recursive(list_of_num):
    """
    A function which calculate numerical sum of a list of numbers
    using recursive method
    Arguments:
    list_of_num - a list containing numbers
    Returns:
    recursively returns the numerical sum of a list of numbers
    """
    # if the size of list is 1 then return the sole element (recursive base case)
    if len(list_of_num) == 1:
        return list_of_num[0]
    # else return the sum of first element and the sum of the rest of the element (recursive call)
    else:
        return list_of_num[0] + _sum_of_list_recursive(list_of_num[1:])

def factorial(n, method = "recursive"):
    """
    A function to compute factorial
    Arguments:
    n - number whose factorial we want to calculate
    Returns:
    fact - factorial of n
    """
    if method == "recursive":
        return _factorial_iterative(n)
    elif method == "iterative":
        return _factorial_recursive(n)
    else:
        return _factorial_recursive(n)

def _factorial_iterative(n):
    """
    A function to compute factorial iteratively
    Arguments:
    n - number whose factorial we want to calculate
    Returns:
    fact - factorial of n
    """
    # a variable to store the factorial, initialized to 1
    fact = 1
    # iterate from 1 to n, and calculate factorial by accumulating products
    for i in range(1, n+1):
        fact *=i
    # return factorial
    return fact

def _factorial_recursive(n):
    """
    A function to compute factorial recursively
    Arguments:
    n - number whose factorial we want to calculate
    Returns:
    factorial of n
    """
    # check for base case
    if n<1:
        return 1
    # else make recursive call
    else:
        return n*_factorial_recursive(n-1)


def power(num, pow):
    """
    A function which computes power of a number
    Arguments:
    num - number whose power is calculated
    pow - number by which the power is raised
    Returns:
    power or exponent of a number
    """
    # if the method is iterative
    if method == "iterative":
        return _power_iterative(num, pow)


def _power_iterative(num, pow):
    """
    A function which computes power of a number iteratively
    Arguments:
    num - number whose power is calculated
    pow - number by which the power is raised
    Returns:
    exponent - power or exponent of a number
    """
    # a variable to accumulate exponent
    exponent = 1
    # accumulate the exponent by iteratively multiplying
    for i in range(pow):
        exponent *= num
    # return the exponent
    return exponent
