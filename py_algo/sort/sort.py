
def sort_list(list_of_items, method = "bubble"):
    """
    A function which sorts a list of numberic values
    Arguments:
    list_of_items - list of items to be sorted
    method - sort method
    Returns:
    list_of_items - sorted list
    """
    if method == "bubble":
        return _bubble_sort(list_of_items)


def _bubble_sort(list_of_items):
    """
    A function which implements bubble sort
    Arguments:
    list_of_items - list of items to be sorted
    Returns:
    list_of_items - sorted list
    """
    # iterate through decreasing number of passes
    for num_of_pass in range(len(list_of_items)-1, 0,-1):
        # iterate number of pass times
        for i in range(num_of_pass):
            # if ith element is greater than (i+1)th element then make a swap
            if list_of_items[i]>list_of_items[i+1]:
                temp = list_of_items[i]
                list_of_items[i] = list_of_items[i+1]
                list_of_items[i+1] = temp
    # return sorted list
    return list_of_items
