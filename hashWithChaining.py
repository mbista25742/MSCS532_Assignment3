import random

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        # Universal hash function parameters
        self.p = 109345121 
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def _hash_function(self, key):
        """Universal hashing function."""
        return ((self.a * hash(key) + self.b) % self.p) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table, replacing if the key already exists."""
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Check if the key already exists and replace its value if found
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # If key was not found, append a new key-value pair
        bucket.append((key, value))

    def search(self, key):
        """Search for a value with the given key in the hash table."""
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Search for the key in the bucket
        for k, v in bucket:
            if k == key:
                return v
        # Return None if key is not found
        return None  

    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Remove key if it exists in the bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

    def __str__(self):
        """String representation for the hash table."""
        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.table))


# Usage example:
hash_table = HashTable(size=10)

# Insert different animals with their respective values
hash_table.insert("lion", 300)
hash_table.insert("tiger", 250)
hash_table.insert("elephant", 500)
hash_table.insert("giraffe", 150)
hash_table.insert("zebra", 100)
hash_table.insert("monkey", 75)
hash_table.insert("panda", 120)
hash_table.insert("koala", 90)
hash_table.insert("kangaroo", 200)
hash_table.insert("rhino", 450)
hash_table.insert("bear", 320)
hash_table.insert("wolf", 270)
hash_table.insert("fox", 220)
hash_table.insert("cheetah", 330)
hash_table.insert("leopard", 310)

# Print the hash table to see chaining in action
print("Hash Table After Inserting Animals:")
print(hash_table)

# Sample search results to verify that entries are accessible
print("\nSearch Results:")
print("lion:", hash_table.search("lion"))
print("tiger:", hash_table.search("tiger"))
print("bear:", hash_table.search("bear"))
print("panda:", hash_table.search("panda"))
print("leopard:", hash_table.search("leopard"))

# Delete some entries
hash_table.delete("tiger")
hash_table.delete("panda")

# Print the hash table after deletion
print("\nHash Table After Deletions:")
print(hash_table)

# Verify deletion
print("\nSearch Results After Deletions:")
print("tiger:", hash_table.search("tiger"))
print("panda:", hash_table.search("panda"))
