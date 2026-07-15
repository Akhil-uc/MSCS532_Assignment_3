
def partition(arr, low, high):
    """
    Partition using first element as pivot.
    """
    pivot = arr[low]
    left = low + 1
    right = high
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            break
        arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        deterministic_quicksort(arr, low, pivot - 1)
        deterministic_quicksort(arr, pivot + 1, high)

if __name__ == "__main__":
    data = [7, 3, 8, 2, 5, 1, 9, 4, 6]
    print("Original Array:")
    print(data)
    deterministic_quicksort(data, 0, len(data) - 1)
    print("\nSorted Array:")
    print(data)