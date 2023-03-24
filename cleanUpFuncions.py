def coverging_pointers(garbage_value, list_to_clean):
    legit = len(list_to_clean) - 1
    left = 0
    right = len(list_to_clean) - 1
    while left < right:
        if list_to_clean[left] != garbage_value:
            left += 1
        else:
            legit -= 1
            list_to_clean[left] = list_to_clean[right]
            right -= 1
    if list_to_clean[left] == garbage_value:
        legit -= 1
    return list_to_clean[:legit + 1]

def copy_over(garbage_value, list_to_clean):
    left = 0
    new_list = []
    while left < len(list_to_clean):
        if list_to_clean[left] != garbage_value:
            new_list.append(list_to_clean[left])
        left += 1
    return new_list
