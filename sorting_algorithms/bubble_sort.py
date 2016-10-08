def bubble_sort(a_list):
    """Sorts a given list using the bubble sort algorithm.
    
    :param a_list: A list containing numbers
    :return: a_list sorted
    """
    for i in range(0, len(a_list)):
        swapped = False
        for j in range(1, len(a_list)):
            if a_list[j] < a_list[j - 1]:
                tmp = a_list[j - 1]
                a_list[j - 1] = a_list[j]
                a_list[j] = tmp
                swapped = True
        if not swapped:
            break

    return a_list

