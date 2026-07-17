# Partition the array using the first element as the pivot
def partition(arr, low, high):

    # Choose the first element as pivot
    pivot = arr[low]
    left = low + 1
    right = high

    while True:

        # Move left pointer until an element greater than pivot is found
        while left <= right and arr[left] <= pivot:
            left += 1

        # Move right pointer until an element smaller than pivot is found
        while left <= right and arr[right] >= pivot:
            right -= 1

        # Stop when pointers cross
        if left > right:
            break

        # Swap misplaced elements
        arr[left], arr[right] = arr[right], arr[left]

    # Place pivot in its correct position
    arr[low], arr[right] = arr[right], arr[low]

    return right


# Recursive Deterministic QuickSort
def deterministic_quicksort(arr, low, high):

    if low < high:

        # Partition the array
        pivot = partition(arr, low, high)

        # Sort left subarray
        deterministic_quicksort(arr, low, pivot - 1)

        # Sort right subarray
        deterministic_quicksort(arr, pivot + 1, high)


# Example execution
if __name__ == "__main__":

    data = [7, 3, 8, 2, 5, 1, 9, 4, 6]

    print("Original Array:")
    print(data)

    deterministic_quicksort(data, 0, len(data) - 1)

    print("\nSorted Array:")
    print(data)
