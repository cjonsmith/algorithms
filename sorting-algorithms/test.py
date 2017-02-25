import quicksort
import random

x = [random.randint(0, 100) for x in range(100)]
print(sorted(x) == quicksort.quicksort(x))
