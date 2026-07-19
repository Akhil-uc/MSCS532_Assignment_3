# Import the random module to generate random pivot positions.
import random


# Define a function that partitions the array around a pivot element.
def partition(arr, low, high):

    # Select the last element in the current subarray as the pivot.
    pivot = arr[high]

    # Initialize a pointer to track the position of smaller elements.
    i = low - 1

    # Loop through every element except the pivot.
    for j in range(low, high):

        # Check whether the current element is less than or equal to the pivot.
        if arr[j] <= pivot:

            # Move the smaller element boundary one position to the right.
            i += 1

            # Swap the current element with the element at the smaller element boundary.
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot into its correct sorted position.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the final position of the pivot.
    return i + 1


# Define a function that selects a random pivot before partitioning the array.
def randomized_partition(arr, low, high):

    # Generate a random index between the low and high positions.
    random_index = random.randint(low, high)

    # Swap the randomly selected pivot with the last element in the subarray.
    arr[random_index], arr[high] = arr[high], arr[random_index]

    # Partition the array using the randomly selected pivot.
    return partition(arr, low, high)


# Define the recursive Randomized QuickSort function.
def randomized_quicksort(arr, low, high):

    # Check whether the current subarray contains more than one element.
    if low < high:

        # Partition the array using a randomly selected pivot.
        pivot = randomized_partition(arr, low, high)

        # Recursively sort the elements to the left of the pivot.
        randomized_quicksort(arr, low, pivot - 1)

        # Recursively sort the elements to the right of the pivot.
        randomized_quicksort(arr, pivot + 1, high)


# Check whether this file is being run directly.
if __name__ == "__main__":

    # Create an example list of unsorted numbers.
    data = [7, 3, 8, 2, 5, 1, 9, 4, 6]

    # Display a heading before printing the original array.
    print("Original Array:")

    # Print the unsorted array.
    print(data)

    # Call the Randomized QuickSort function to sort the entire array.
    randomized_quicksort(data, 0, len(data) - 1)

    # Display a heading before printing the sorted array.
    print("\nSorted Array:")

    # Print the sorted array.
    print(data)
