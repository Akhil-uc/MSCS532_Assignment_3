# Hash table implementation using separate chaining
class HashTable:

    # Initialize the hash table
    def __init__(self, size=10):

        self.size = size

        # Create empty buckets
        self.table = [[] for _ in range(size)]

    # Compute the hash index
    def hash_function(self, key):

        return hash(key) % self.size

    # Insert or update a key-value pair
    def insert(self, key, value):

        index = self.hash_function(key)

        bucket = self.table[index]

        # Update value if key already exists
        for pair in bucket:

            if pair[0] == key:
                pair[1] = value
                return

        # Otherwise add a new pair
        bucket.append([key, value])

    # Search for a key
    def search(self, key):

        index = self.hash_function(key)

        bucket = self.table[index]

        for pair in bucket:

            if pair[0] == key:
                return pair[1]

        return None

    # Delete a key-value pair
    def delete(self, key):

        index = self.hash_function(key)

        bucket = self.table[index]

        for i, pair in enumerate(bucket):

            if pair[0] == key:
                del bucket[i]
                return True

        return False

    # Display all buckets
    def display(self):

        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)


# Example execution
if __name__ == "__main__":

    ht = HashTable(7)

    ht.insert("Apple", 120)
    ht.insert("Banana", 50)
    ht.insert("Orange", 80)
    ht.insert("Mango", 150)

    print("Hash Table")
    ht.display()

    print("\nSearch Mango:")
    print(ht.search("Mango"))

    print("\nDeleting Banana")
    ht.delete("Banana")

    ht.display()
