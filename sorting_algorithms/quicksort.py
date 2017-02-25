
def quicksort(collection):
    """Sorts a list using the quicksort algorithm.
        
     Parmeters:
        collection - The collection to be sorted.
        
    Return:
        The sorted collection.
    """

    # Base case: if the collection is empty, return an empty collection.
    if len(collection) == 0:
        return []

    # Let the pivot be position 0 in collection. Find all values less than or equal to the pivot and create a separate
    # list with these values then recursively call quicksort on that list. Do the same for the values greater than the
    # pivot.
    pivot = collection[0]
    left = quicksort([x for x in collection[1:] if x <= pivot])
    right = quicksort([x for x in collection[1:] if x > pivot])

    # Once both sides of the list are sorted, concatenate the lists with the pivot in the middle and return it.
    collection = left + collection[0:1] + right
    return collection
