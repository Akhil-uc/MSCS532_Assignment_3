import random
def partition(arr, low, high):
    """
    Partitions the array around the pivot.
    Parameters
    ----------
    arr : list
        List to be sorted.
    low : int
        Starting index.
    high : int
        Ending index.
    Returns
    -------
    int
        Final position of pivot.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def randomized_partition(arr, low, high):
    """
    Selects a random pivot and partitions the array.
    """
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)


def randomized_quicksort(arr, low, high):
    """
    Recursive Randomized Quicksort.
    """
    if low < high:
        pivot = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot - 1)
        randomized_quicksort(arr, pivot + 1, high)


if __name__ == "__main__":
    data = [7, 3, 8, 2, 5, 1, 9, 4, 6]
    print("Original Array:")
    print(data)
    randomized_quicksort(data, 0, len(data) - 1)
    print("\nSorted Array:")
    print(data)