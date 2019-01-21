
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
