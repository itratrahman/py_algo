
def search(list_of_items, search_item, method = "sequential"):
    """
    A function which implements search method
    Arguments:
    list_of_items - list containing the possible search item
    search_item - the search item
    Returns:
    item_found - boolean variable to indicate whether the search item is found
    """
    if method = "sequential":
        return  _sequential_search(list_of_items, search_item)



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
    item_found = False
    # iterate though each item in the list
    for item in list_of_items:
        # item is found then set the indicator variable to True
        if item == search_item:
            item_found = True
        # else set the indicator variable to False
        else:
            item_found = False
    # return the indicator variable
    return item_found
