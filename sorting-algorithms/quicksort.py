def quicksort(collection):
    """Sorts a collection using quicksort.
    
    Parameters:
        collection - A collection to sort.
    
    Returns:
        The sorted collection.
    """
    # Base case: if the collection contains a single element, return an empty type of the collection.
    if len(collection) == 0:
        return type(collection)()

    # Pick a pivot, which is the first element, in this implementation.
    pivot = collection[0]

    # Recursively call quicksort on the subsets of the collection to the left and right of the collection.
    left = quicksort([x for x in collection if x < pivot])
    right = quicksort([x for x in collection if x > pivot])

    left.append(pivot)
    return left + right
