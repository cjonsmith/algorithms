from time import time
from random import shuffle

def bogosort(to_sort, to_time=False):
    """Sorts an iterable using the infamous bogosort algorithm.

    Parameters:
        to_sort - An iterable to be sorted.
        to_time - A flag to determine if you want to know how long this really
        takes.
    Returns:
        The sorted iterable.
    """
    start = time()
    # While extremely inefficient, it sure is easy to write.
    # Be sure to sort the list at each pass in the while loop to make it extra
    # inefficient!
    while sorted(to_sort) != to_sort:
        shuffle(to_sort)
    end = time()
    if to_time: 
        print("Sorted collection of length {} in {} {}.".format(
            len(to_sort),
            end - start if end - start < 120 else (end - start) // 60,
            "seconds" if end - start < 120 else "minutes.")
        )
