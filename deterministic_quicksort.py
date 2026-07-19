# Define a function that partitions the array around a pivot element.
def partition(arr, low, high):

    # Select the first element in the current subarray as the pivot.
    pivot = arr[low]

    # Set the left pointer to the element immediately after the pivot.
    left = low + 1

    # Set the right pointer to the last element of the current subarray.
    right = high

    # Continue searching until the pointers cross.
    while True:

        # Move the left pointer while it stays within the array
        # and the current value is less than or equal to the pivot.
        while left <= right and arr[left] <= pivot:

            # Move the left pointer one position to the right.
            left += 1

        # Move the right pointer while it stays within the array
        # and the current value is greater than or equal to the pivot.
        while left <= right and arr[right] >= pivot:

            # Move the right pointer one position to the left.
            right -= 1

        # Check whether the two pointers have crossed each other.
        if left > right:

            # Exit the loop because partitioning is complete.
            break

        # Swap the misplaced elements so they move to the correct side of the pivot.
        arr[left], arr[right] = arr[right], arr[left]

    # Place the pivot into its correct sorted position.
    arr[low], arr[right] = arr[right], arr[low]

    # Return the final position of the pivot.
    return right


# Define the recursive Deterministic QuickSort function.
def deterministic_quicksort(arr, low, high):

    # Check whether the current subarray contains more than one element.
    if low < high:

        # Partition the current subarray and get the pivot's final position.
        pivot = partition(arr, low, high)

        # Recursively sort all elements to the left of the pivot.
        deterministic_quicksort(arr, low, pivot - 1)

        # Recursively sort all elements to the right of the pivot.
        deterministic_quicksort(arr, pivot + 1, high)


# Check whether this file is being run directly.
if __name__ == "__main__":

    # Create an example list of unsorted numbers.
    data = [7, 3, 8, 2, 5, 1, 9, 4, 6]

    # Display a heading before printing the original array.
    print("Original Array:")

    # Print the unsorted array.
    print(data)

    # Call the QuickSort function to sort the entire array.
    deterministic_quicksort(data, 0, len(data) - 1)

    # Display a heading before printing the sorted array.
    print("\nSorted Array:")

    # Print the sorted array.
    print(data)
