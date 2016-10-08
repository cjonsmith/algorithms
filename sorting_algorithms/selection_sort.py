def selection_sort(a_list):
    """Sorts a given list using the selection sort algorithm.

    :param a_list: The list to sort.
    :return: The sorted list."""
    end_position = len(a_list) # The position to swap with largest found value

    while end_position != 0:
        # Traverse the unsorted portion of the list to find the largest value in it.
        # Save the largest value and its position in the list as well.
        largest = a_list[0], 0
        for i, value in enumerate(a_list[:end_position]):
            if value > largest[0]:
                largest = value, i

        # Preseve the element at end of the unsorted portion of the list, then swap
        # it with the largest element.
        tmp = a_list[end_position - 1]
        a_list[end_position - 1] = largest[0]
        a_list[largest[1]] = tmp

        end_position -= 1 # Decrease the size of the unsorted array
    
    return a_list

