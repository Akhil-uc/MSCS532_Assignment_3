import random

# Standard partition function
def partition(arr, low, high):

    # Choose the last element as pivot
    pivot = arr[high]

    i = low - 1

    # Move smaller elements before the pivot
    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Select a random pivot before partitioning
def randomized_partition(arr, low, high):

    # Pick a random pivot index
    random_index = random.randint(low, high)

    # Move random pivot to the end
    arr[random_index], arr[high] = arr[high], arr[random_index]

    return partition(arr, low, high)


# Recursive Randomized QuickSort
def randomized_quicksort(arr, low, high):

    if low < high:

        # Partition the array using a random pivot
        pivot = randomized_partition(arr, low, high)

        # Sort left half
        randomized_quicksort(arr, low, pivot - 1)

        # Sort right half
        randomized_quicksort(arr, pivot + 1, high)


# Example execution
if __name__ == "__main__":

    data = [7, 3, 8, 2, 5, 1, 9, 4, 6]

    print("Original Array:")
    print(data)

    randomized_quicksort(data, 0, len(data) - 1)

    print("\nSorted Array:")
    print(data)
