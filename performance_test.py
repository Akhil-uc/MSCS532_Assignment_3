import random
import time
import sys

from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort
sys.setrecursionlimit(20000)


def measure(sort_function, array):
    """
    Measure execution time of a sorting algorithm.

    Parameters
    ----------
    sort_function : function
        Sorting function to test.
    array : list
        Input array.

    Returns
    -------
    float or str
        Execution time in seconds, or an error message if
        recursion depth is exceeded.
    """

    arr = array.copy()

    start = time.perf_counter()

    try:
        sort_function(arr, 0, len(arr) - 1)
        end = time.perf_counter()
        return f"{end - start:.6f} seconds"

    except RecursionError:
        return "RecursionError (Worst Case)"


sizes = [1000, 5000, 10000]

for n in sizes:

    print("=" * 60)
    print(f"Array Size: {n}")
    print("=" * 60)

    random_array = [random.randint(1, 100000) for _ in range(n)]
    sorted_array = list(range(n))
    reverse_array = list(range(n, 0, -1))
    duplicate_array = [5] * n

    print("\nRandom Array")
    print(f"Randomized     : {measure(randomized_quicksort, random_array)}")
    print(f"Deterministic  : {measure(deterministic_quicksort, random_array)}")

    print("\nSorted Array")
    print(f"Randomized     : {measure(randomized_quicksort, sorted_array)}")
    print(f"Deterministic  : {measure(deterministic_quicksort, sorted_array)}")

    print("\nReverse Sorted Array")
    print(f"Randomized     : {measure(randomized_quicksort, reverse_array)}")
    print(f"Deterministic  : {measure(deterministic_quicksort, reverse_array)}")

    print("\nDuplicate Array")
    print(f"Randomized     : {measure(randomized_quicksort, duplicate_array)}")
    print(f"Deterministic  : {measure(deterministic_quicksort, duplicate_array)}")

    print()