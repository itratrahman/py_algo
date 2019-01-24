
def sort(list_of_items, method = "bubble"):
    """
    A function which sorts a list of numberic values
    Arguments:
    list_of_items - list of items to be sorted
    Returns:
    list_of_items - sorted list
    """
    if method == "bubble":
        return _bubble_sort(list_of_items)
