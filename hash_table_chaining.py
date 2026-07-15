
class HashTable:

    def __init__(self, size=10):
        """
        Create empty hash table.
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """
        Compute index using built-in hash.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert key-value pair.
        If key already exists,
        update its value.
        """
        index = self.hash_function(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def search(self, key):
        """
        Search for a key.
        Returns value if found.
        """
        index = self.hash_function(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        """
        Delete a key-value pair.
        """
        index = self.hash_function(key)
        bucket = self.table[index]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return True
        return False

    def display(self):
        """
        Print complete hash table.
        """
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)


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