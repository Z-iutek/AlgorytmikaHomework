def binary_search(list_to_search, value_to_find):
    lo = 0
    hi = len(list_to_search) - 1

    while hi - lo > 1:
        mid = (hi + lo) // 2
        if list_to_search[mid] < value_to_find:
            lo = mid + 1
        else:
            hi = mid

    if list_to_search[lo] == value_to_find:
        index_value = lo
    elif list_to_search[hi] == value_to_find:
        index_value = hi
    else:
        index_value = -1

    return index_value


def linear_search(list_to_search, value_to_find):
    for i in range(0, len(list_to_search) - 1):
        if list_to_search[i] == value_to_find:
            return i
    return -1
