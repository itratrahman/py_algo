
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
        # recursive call on left and righ half of the array
        _split_and_merge(left_half)
        _split_and_merge(right_half)

        ###########Merge Operation###########
        # indexes for merging
        i,j,k = 0,0,0
        # merge of by comparing the left & right half of the merged list
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                list_of_items[k] = left_half[i]
                i += 1
            else:
                list_of_items[k] = right_half[j]
                j += 1
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


def _quick_sort(alist):
    """
    A function which invokes _split_and_partition function
    which invokes quick sort operation
    Arguments:
    list_of_items - list of items to be sorted
    Returns:
    list_of_items - sorted list
    """
    # invoke recursive function to recursively split and partition
    _split_and_partition(alist,0,len(alist)-1)
    # return the sorted list
    return alist


def _split_and_partition(alist,first,last):
    """
    A function which implements recursively split and partition
    to implement quick sort
    Arguments:
    list_of_items - list of items to be sorted
    """
    # if first element is less than last element
    # then recursively split and partion to sort
    if first<last:
        splitpoint = partition(alist,first,last)
        # recursive call on left and right of partition
        _split_and_partition(alist,first,splitpoint-1)
        _split_and_partition(alist,splitpoint+1,last)


def partition(alist,first,last):
    """
    A function to partition for quick sort
    """
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark
