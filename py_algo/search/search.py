
def search(list_of_items, search_item, method = "sequential"):
    """
    A function which implements search method
    Arguments:
    list_of_items - list containing the possible search item
    search_item - the search item
    Returns:
    item_found - boolean variable to indicate whether the search item is found
    """
    # if method is sequential
    if method == "sequential":
        return  _sequential_search(list_of_items, search_item)
    # if the method is binary search
    elif method == "binary":
        return  _binary_search_iterative(list_of_items, search_item)
    # if the method is binary search iterative
    elif method == "binary_iterative":
        return  _binary_search_iterative(list_of_items, search_item)
    # if the method is binary search recursive
    elif method == "binary_recursive":
        return _binary_search_recursive(list_of_items, search_item)
    # else use binary search recursive
    else:
        return _binary_search_recursive(list_of_items, search_item)

def _sequential_search(list_of_items, search_item):
    """
    A function which implements sequential search
    Arguments:
    list_of_items - list containing the possible search item
    search_item - the search item
    Returns:
    item_found - boolean variable to indicate whether the search item is found
    """
    # boolean variable to indicate whether the search item is found
    # indicator variable is initialize to false
    found = False
    # running index
    index = 0
    # while we have not run out of list items and item is not found
    while index < len(list_of_items) and not found:
        # if the search item is found then set indicator variable to True
        if list_of_items[index] == search_item:
            found = True
        # else increment the running index
        else:
            index = index+1
    # return the indicator variable
    return found

def _binary_search_iterative(list_of_items, search_item):
    """
    A function which implements binary search(iterative)
    Arguments:
    list_of_items - list containing the possible search item
    search_item - the search item
    Returns:
    item_found - boolean variable to indicate whether the search item is found
    """
    # initialize the first & last index
    first_index = 0
    last_index = len(list_of_items)-1
    # boolean variable to indicate whether the search item is found
    # indicator variable is initialize to false
    item_found = False
    # while the item is not found and we have not run out of list
    while not item_found and first_index<=last_index:
        # calculate index of the midpoint
        midpoint_index = (first_index+last_index)//2
        # if the item is found then set indicator variable to True
        if list_of_items[midpoint_index] == search_item:
            item_found = True
        # check the posistion of the search item relative to the midpoint
        else:
            # if the search item is less than midpoint than
            # update less index to one less than midpoint index
            if search_item < list_of_items[midpoint_index]:
                last_index = midpoint_index-1
            # else update the first index to one above midpoint index
            else:
                first_index = midpoint_index + 1
    # return the indicator variable
    return item_found

def _binary_search_recursive(list_of_items, search_item):
    """
    A function which implements binary search(recursive)
    Arguments:
    list_of_items - list containing the possible search item
    search_item - the search item
    Returns:
    item_found - boolean variable to indicate whether the search item is found
    """
    # if the length of list_of_items is zero then return False
    if len(list_of_items) == 0:
        return False
    # or else search recursively
    else:
        # calculate index of the midpoint
        midpoint_index = len(list_of_items)//2
        # if the midpoint item is the search item then return True
        if list_of_items[midpoint_index]==search_item:
            return True
        # else make recursive calls
        else:
            # if the search item is in the lower half
            # then make recursive call to the lower half of the list
            if search_item<list_of_items[midpoint_index]:
                return _binary_search_recursive(list_of_items[:midpoint_index], search_item)
            # if the search item is in the upper half
            # then make recursive call to the upper half of the list
            else:
                return _binary_search_recursive(list_of_items[midpoint_index+1:], search_item)
