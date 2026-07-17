# Import required modules
import random
import time
import sys

# Import QuickSort implementations
from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort

# Increase recursion limit for large inputs
sys.setrecursionlimit(20000)


# Measure execution time of a sorting algorithm
def measure(sort_function, array):

    # Work on a copy so the original array remains unchanged
    arr = array.copy()

    # Start timer
    start = time.perf_counter()

    try:

        # Execute sorting algorithm
        sort_function(arr, 0, len(arr) - 1)

        # Stop timer
        end = time.perf_counter()

        return f"{end - start:.6f} seconds"

    # Handle worst-case recursion depth
    except RecursionError:

        return "RecursionError (Worst Case)"


# Different input sizes
sizes = [1000, 5000, 10000]

# Test each input size
for n in sizes:

    print("=" * 60)
    print(f"Array Size: {n}")
    print("=" * 60)

    # Generate different types of input arrays
    random_array = [random.randint(1, 100000) for _ in range(n)]
    sorted_array = list(range(n))
    reverse_array = list(range(n, 0, -1))
    duplicate_array = [5] * n

    # Test random array
    print("\nRandom Array")
    print(f"Randomized     : {measure(randomized_quicksort, random_array)}")
    print(f"Deterministic  : {measure(deterministic_quicksort, random_array)}")

    # Test sorted array
    print("\nSorted Array")
    print(f"Randomized     : {measure(randomized_quicksort, sorted_array)}")
    print(f"Deterministic  : {measure(deterministic_quicksort, sorted_array)}")

    # Test reverse sorted array
    print("\nReverse Sorted Array")
    print(f"Randomized     : {measure(randomized_quicksort, reverse_array)}")
    print(f"Deterministic  : {measure(deterministic_quicksort, reverse_array)}")

    # Test duplicate array
    print("\nDuplicate Array")
    print(f"Randomized     : {measure(randomized_quicksort, duplicate_array)}")
    print(f"Deterministic  : {measure(deterministic_quicksort, duplicate_array)}")

    print()
