
def power(num, pow, method='iterative'):
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
    elif method == "recursive":
        return _power_recursive(num, pow)
    else:
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


def _power_recursive(num, pow):
    """
    A function which computes power of a number recursively
    Arguments:
    num - number whose power is calculated
    pow - number by which the power is raised
    Returns:
    exponent - power or exponent of a number
    """
    # power is zero then it is the base case
    # so return 1
    if pow == 0:
        return 1
    # else make recursive call
    else:
        return num*_power_recursive(num,pow-1)
