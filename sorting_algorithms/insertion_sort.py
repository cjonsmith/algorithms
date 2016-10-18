def insertion_sort(a_list):
    """Sorts a given list in place using the insertion sort algorithm.

    :param a_list: The list to be sorted
    :return: The sorted list
    """
    # Start at the second element since the first element is considered sorted.
    for i in range(1, len(a_list)):
        
        # Check if the current element is ever greater than any of the previous
        # elements. If it is, continue to swap it backwards into the list.
        for j in range(i, 0, -1):
            if a_list[j] < a_list[j - 1]:
                a_list[j], a_list[j - 1] = a_list[j - 1], a_list[j]
            # If the current element is greater than the previous element, then
            # we know the list is in the correct order, since the inner loop only
            # operates on the sorted portion of the list.
            else:
                break
    
    return a_list

