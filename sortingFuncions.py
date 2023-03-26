def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):

        key = list_to_sort[i]
        j = i - 1
        while j >= 0 and key < list_to_sort[j]:
            list_to_sort[j + 1] = list_to_sort[j]
            j -= 1
        list_to_sort[j + 1] = key
    return list_to_sort


def merge_sort(list_to_sort):
    if len(list_to_sort) > 1:

        mid = len(list_to_sort) // 2

        left = list_to_sort[:mid]

        right = list_to_sort[mid:]

        merge_sort(left)

        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list_to_sort[k] = left[i]
                i += 1
            else:
                list_to_sort[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list_to_sort[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list_to_sort[k] = right[j]
            j += 1
            k += 1
    return list_to_sort
