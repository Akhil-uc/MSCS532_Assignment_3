# Import the random module to generate random test data.
import random

# Import the time module to measure algorithm execution time.
import time

# Import the sys module to modify the recursion limit.
import sys

# Import the Randomized QuickSort implementation.
from randomized_quicksort import randomized_quicksort

# Import the Deterministic QuickSort implementation.
from deterministic_quicksort import deterministic_quicksort

# Increase the recursion limit so larger arrays can be sorted without reaching Python's default recursion depth.
sys.setrecursionlimit(20000)


# Define a function that measures the execution time of a sorting algorithm.
def measure(sort_function, array):

    # Create a copy of the input array so the original data is not modified.
    arr = array.copy()

    # Record the current time before sorting begins.
    start = time.perf_counter()

    # Attempt to execute the sorting algorithm.
    try:

        # Sort the copied array using the selected sorting function.
        sort_function(arr, 0, len(arr) - 1)

        # Record the current time after sorting finishes.
        end = time.perf_counter()

        # Calculate and return the total execution time.
        return f"{end - start:.6f} seconds"

    # Handle the situation where the recursion limit is exceeded.
    except RecursionError:

        # Return a message indicating that the worst-case recursion depth was reached.
        return "RecursionError (Worst Case)"


# Create a list containing the array sizes that will be tested.
sizes = [1000, 5000, 10000]

# Loop through each array size in the list.
for n in sizes:

    # Print a separator line for better readability.
    print("=" * 60)

    # Display the current array size being tested.
    print(f"Array Size: {n}")

    # Print another separator line.
    print("=" * 60)

    # Generate an array containing random values.
    random_array = [random.randint(1, 100000) for _ in range(n)]

    # Generate an array that is already sorted in ascending order.
    sorted_array = list(range(n))

    # Generate an array sorted in descending order.
    reverse_array = list(range(n, 0, -1))

    # Generate an array containing duplicate values.
    duplicate_array = [5] * n

    # Display a heading before testing the random array.
    print("\nRandom Array")

    # Measure and display the execution time of Randomized QuickSort.
    print(f"Randomized     : {measure(randomized_quicksort, random_array)}")

    # Measure and display the execution time of Deterministic QuickSort.
    print(f"Deterministic  : {measure(deterministic_quicksort, random_array)}")

    # Display a heading before testing the sorted array.
    print("\nSorted Array")

    # Measure and display the execution time of Randomized QuickSort.
    print(f"Randomized     : {measure(randomized_quicksort, sorted_array)}")

    # Measure and display the execution time of Deterministic QuickSort.
    print(f"Deterministic  : {measure(deterministic_quicksort, sorted_array)}")

    # Display a heading before testing the reverse sorted array.
    print("\nReverse Sorted Array")

    # Measure and display the execution time of Randomized QuickSort.
    print(f"Randomized     : {measure(randomized_quicksort, reverse_array)}")

    # Measure and display the execution time of Deterministic QuickSort.
    print(f"Deterministic  : {measure(deterministic_quicksort, reverse_array)}")

    # Display a heading before testing the duplicate array.
    print("\nDuplicate Array")

    # Measure and display the execution time of Randomized QuickSort.
    print(f"Randomized     : {measure(randomized_quicksort, duplicate_array)}")

    # Measure and display the execution time of Deterministic QuickSort.
    print(f"Deterministic  : {measure(deterministic_quicksort, duplicate_array)}")

    # Print a blank line to separate the results for each input size.
    print()
