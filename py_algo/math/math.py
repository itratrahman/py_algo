

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
        return sum_of_list_iterative(list_of_num)
    # if the method is recursive
    elif method == "recursive":
        return sum_of_list_recursive(list_of_num)
    # else use the iterative method to calculate sum
    else:
        return sum_of_list_iterative(list_of_num)


def sum_of_list_iterative(list_of_num):
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


def sum_of_list_recursive(list_of_num):
    """
    A function which calculate numerical sum of a list of numbers
    using recursive method
    Arguments:
    list_of_num - a list containing numbers
    Returns:
    summation - numerical sum of a list of numbers
    """
    # if the size of list is 1 then return the sole element (recursive base case)
    if len(list_of_num) == 1:
        return list_of_num[0]
    # else return the sum of first element and the sum of the rest of the element (recursive call)
    else:
        return list_of_num[0] + sum_of_list_recursive(list_of_num[1:])
