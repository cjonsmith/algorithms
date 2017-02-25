from random import shuffle

def bogosort(to_sort):
    """Sorts a collection using the infamous bogosort algorithm.

    Parameters:
        to_sort - An iterable to be sorted.
    Returns:
        The sorted collection.
    """
    # Be sure to sort the list at each pass in the while loop to make it extra
    # inefficient!
    while sorted(to_sort) != to_sort:
        shuffle(to_sort)
