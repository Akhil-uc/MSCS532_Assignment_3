# Define a HashTable class that uses separate chaining to handle collisions.
class HashTable:

    # Define the constructor that creates a new hash table.
    def __init__(self, size=10):

        # Store the total number of buckets in the hash table.
        self.size = size

        # Create a list containing empty buckets to store key-value pairs.
        self.table = [[] for _ in range(size)]

    # Define a function that calculates the hash index for a given key.
    def hash_function(self, key):

        # Apply Python's hash function and limit the result to the table size.
        return hash(key) % self.size

    # Define a function that inserts a new key-value pair into the hash table.
    def insert(self, key, value):

        # Calculate the bucket index where the key should be stored.
        index = self.hash_function(key)

        # Access the bucket located at the calculated index.
        bucket = self.table[index]

        # Check every key-value pair already stored in the bucket.
        for pair in bucket:

            # Determine whether the current key already exists.
            if pair[0] == key:

                # Update the existing value with the new value.
                pair[1] = value

                # Exit the function because the key has been updated.
                return

        # Add the new key-value pair to the bucket because the key was not found.
        bucket.append([key, value])

    # Define a function that searches for a key in the hash table.
    def search(self, key):

        # Calculate the bucket index for the given key.
        index = self.hash_function(key)

        # Retrieve the bucket located at the calculated index.
        bucket = self.table[index]

        # Examine every key-value pair stored in the bucket.
        for pair in bucket:

            # Check whether the current key matches the requested key.
            if pair[0] == key:

                # Return the value associated with the matching key.
                return pair[1]

        # Return None because the key was not found.
        return None

    # Define a function that removes a key-value pair from the hash table.
    def delete(self, key):

        # Calculate the bucket index for the given key.
        index = self.hash_function(key)

        # Retrieve the bucket located at the calculated index.
        bucket = self.table[index]

        # Loop through the bucket while keeping track of each element's index.
        for i, pair in enumerate(bucket):

            # Check whether the current key matches the key to be deleted.
            if pair[0] == key:

                # Remove the matching key-value pair from the bucket.
                del bucket[i]

                # Return True to indicate that the deletion was successful.
                return True

        # Return False because the key was not found.
        return False

    # Define a function that displays the contents of the hash table.
    def display(self):

        # Loop through every bucket and its corresponding index.
        for i, bucket in enumerate(self.table):

            # Print the bucket index and the key-value pairs stored in that bucket.
            print(i, ":", bucket)


# Check whether this file is being run directly.
if __name__ == "__main__":

    # Create a hash table containing seven buckets.
    ht = HashTable(7)

    # Insert the first key-value pair into the hash table.
    ht.insert("Apple", 120)

    # Insert the second key-value pair into the hash table.
    ht.insert("Banana", 50)

    # Insert the third key-value pair into the hash table.
    ht.insert("Orange", 80)

    # Insert the fourth key-value pair into the hash table.
    ht.insert("Mango", 150)

    # Display a heading before printing the hash table.
    print("Hash Table")

    # Display the contents of every bucket in the hash table.
    ht.display()

    # Display a heading before searching for a key.
    print("\nSearch Mango:")

    # Search for the value associated with the key "Mango" and print the result.
    print(ht.search("Mango"))

    # Display a heading before deleting a key.
    print("\nDeleting Banana")

    # Remove the key "Banana" from the hash table.
    ht.delete("Banana")

    # Display the updated hash table after the deletion.
    ht.display()
