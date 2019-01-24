
def sort_list(list_of_items, method = "merge"):
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
    elif method == "merge":
        _merge_sort(list_of_items)
        return list_of_items
    elif method == "quick":
        return _quick_sort(list_of_items)
    else:
        _merge_sort(list_of_items)
        return list_of_items


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


def _merge_sort(list_of_items, verbose = False):
    """
    A function which invokes _split_and_merge function
    which invokes merge sort operation
    Arguments:
    list_of_items - list of items to be sorted
    Returns:
    list_of_items - sorted list
    """
    _split_and_merge(list_of_items, verbose)
    return list_of_items


def _split_and_merge(list_of_items, verbose = False):
    """
    A function which implements merge sort
    Arguments:
    list_of_items - list of items to be sorted
    """
    if verbose:
        print("Splitting:",list_of_items)

    # if the length of list is greater than one
    # them proceed splitting recursively and merging
    if len(list_of_items)>1:

        ###########Split Operation###########
        # calculate the midpoint
        midpoint = len(list_of_items)//2
        # extract left and right half of the array
        left_half = list_of_items[:midpoint]
        right_half = list_of_items[midpoint:]
        # recursive call on left and righ halves of the array
        _split_and_merge(left_half)
        _split_and_merge(right_half)

        ###########Merge Operation###########
        # indexes for merging
        i,j,k = 0,0,0
        # merge by comparing the left & right half of the merged list
        while i<len(left_half) and j<len(right_half):
            # if the ith elem of left half
            # is less than jth elem of right half
            # initialize the kth elem of list to ith elem of left half
            # increment the i by 1
            if left_half[i]<right_half[j]:
                list_of_items[k] = left_half[i]
                i += 1
            # if the ith elem of left half
            # is greater than jth elem of right half
            # initialize the kth elem of list to ith elem of left half
            # increment the j by 1
            else:
                list_of_items[k] = right_half[j]
                j += 1
            # increment k by 1
            k += 1
        # assign the left overs of left half of the merged list to the the original list
        while i < len(left_half):
            list_of_items[k] = left_half[i]
            i += 1
            k += 1
        # assign the left overs of right half of the merged list to the the original list
        while j < len(right_half):
            list_of_items[k] = right_half[j]
            j += 1
            k += 1

    if verbose:
        print("Merging:", list_of_items)


def _quick_sort(list_of_items):
    """
    A function which invokes _split_and_partition function
    which invokes quick sort operation
    Arguments:
    list_of_items - list of items to be sorted
    Returns:
    list_of_items - sorted list
    """
    # invoke recursive function to recursively split and partition
    _split_and_partition(list_of_items,0,len(list_of_items)-1)
    # return the sorted list
    return list_of_items


def _split_and_partition(list_of_items,first_elem,last_elem):
    """
    A function which implements recursively split and partition
    to implement quick sort
    Arguments:
    list_of_items - list of items to be sorted
    """
    # if first element is less than last element
    # then recursively split and partion to sort
    if first_elem<last_elem:
        splitpoint = partition(list_of_items,first_elem,last_elem)
        # recursive call on left and right of partition
        _split_and_partition(list_of_items,first_elem,splitpoint-1)
        _split_and_partition(list_of_items,splitpoint+1,last_elem)


def partition(list_of_items,first_elem,last_elem):
    """
    A function to partition for quick sort
    """
    # calculate pivot, left mark and right mark
    pivot = list_of_items[first_elem]
    left_mark = first_elem+1
    right_mark = last_elem

    # a boolean variable to indicate whether a partition is found
    partition_found = False
    # iterate until parition is not found
    while not partition_found:
        # increment left mark until we locate a value that is greater than the pivot
        while left_mark <= right_mark and list_of_items[left_mark] <= pivot:
            left_mark = left_mark + 1
        # decrement right mark until we find a value that is less than the pivot
        while list_of_items[right_mark] >= pivot and right_mark >= left_mark:
            right_mark = right_mark -1
        # if the right mark is less left mark then partition is found
        if right_mark < left_mark:
            partition_found = True
        # else swap left and right marks
        else:
            temp = list_of_items[left_mark]
            list_of_items[left_mark] = list_of_items[right_mark]
            list_of_items[right_mark] = temp
    # swap first element and right mark
    temp = list_of_items[first_elem]
    list_of_items[first_elem] = list_of_items[right_mark]
    list_of_items[right_mark] = temp
    # return the right mark which is the splitpoint
    return right_mark
