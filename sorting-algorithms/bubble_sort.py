def bubble_sort(a_list):
    """Sorts a given list in place using the bubble sort algorithm.
    
    :param a_list: A list containing numbers
    :return: a_list sorted
    """
    # Loop over the entire list
    for i, elem in enumerate(a_list):
        # Keep track if a swap has been performed. A slight optimization to bubble
        # sort is to end the operation if an entire pass over the list with no swaps
        # occurring, since this means the data is sorted.
        swapped = False

        # Begin looping over the data again, swapping when the current element is
        # smaller than the previous element.
        for j, next_elem in enumerate(a_list[1:]):
            if next_elem < elem:
                a_list[j], a_list[i] = a_list[i], a_list[j]
                swapped = True
        # End sort function if no swaps occurred.
        if not swapped:
            break

    return a_list

