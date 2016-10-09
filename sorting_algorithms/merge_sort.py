def merge(list1, list2):
    """Merges two lists together in order.
    
    :param list1: The first list.
    :param list2: The second list.
    :return: The sorted merge of list1 and list2.
    """
    merged = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] <= list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))
    
    while len(list1) > 0:
        merged.append(list1.pop(0))
    while len(list2) > 0:
        merged.append(list2.pop(0))
    
    return merged

def merge_sort(a_list):
    """Sorts a list using the merge sort algorithm.
    
    :param a_list: The list to be sorted.
    :return: The sorted list
    """
    # Base case: Only one element in list.
    if len(a_list) == 1:
        return a_list

    # Split the list into two halves
    mid = len(a_list) // 2
    left_half = a_list[:mid]
    right_half = a_list[mid:]

    # Sort each individual halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

