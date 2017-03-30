import quicksort
import bubble_sort
import random

print('Quicksort:')
x = [random.randint(0, 100) for x in range(100)]
print(sorted(x) == quicksort.quicksort(x))

print('Bubble Sort:')
x = [random.randrange(100) for x in range(100)]
print(sorted(x) == bubble_sort.bubble_sort(x))

