class HashTable:
    def __init__(self, size):
        """
        constructor method, initialize hash table
        :param size: the size of the hash table
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        compute the hash value for a given key. sum the ascii values of the key's char, then multiply by the size of the array
        :param key: string key for which we calculate the hash
        :return: the hash val
        """
        key_sum = sum(ord(char) for char in key)
        return key_sum % self.size

    def insert(self, key, value):
        """
        insert key-value pair into the hash, update already existing ones
        :param key: string key
        :param value: value associated with the key
        :return:
        """
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update the existing key's value
                return

        # If the key does not exist in the list, append it as a new key-value pair
        self.table[index].append((key, value))

    def get(self, key):
        """
        retrieve the value associated with a given key
        :param key: the key
        :return: the value, or none
        """
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None  # Key not found#

    def delete(self, key):
        """
        delete a key-value pair from the table
        :param key: the key
        :return: the value associated with that deleted key, or none
        """
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return v

    def items(self):
        """
        Return a list of (key, value) pairs from the hash table.
        """
        items_list = []
        for slot in self.table:
            if slot is not None:
                for key, value in slot:
                    items_list.append((key, value))
        return items_list
#
# table = HashTable(size=5)
#
# # Test insert and get methods
# table.insert("apple", 5)
# print("Inserted 'apple':", table.get("apple") == 5)
# # Test inserting and getting multiple items
# table.insert("banana", 2)
# table.insert("cherry", 7)
# print("Inserted 'banana' and 'cherry':", table.get("banana") == 2 and table.get("cherry") == 7)
#
# # Test updating an existing key
# table.insert("apple", 10)
# print("Updated 'apple':", table.get("apple") == 10)
#
# # Test getting a key that doesn't exist
# print("Getting 'grape' (expecting None):", table.get("grape") is None)
#
# # Test delete method
# deleted_value = table.delete("banana")
# print("Deleted 'banana' (expecting 2):", deleted_value == 2)
# print("Getting 'banana' after deletion (expecting None):", table.get("banana") is None)
#
# # Test delete on a key that doesn't exist
# deleted_value = table.delete("watermelon")
# print("Deleted 'watermelon' (expecting None):", deleted_value is None)
# # Test hash collisions
# table.insert("dog", "poodle")
# table.insert("god", "labrador")
# print("Inserted 'dog' and 'god':", table.get("dog") == "poodle" and table.get("god") == "labrador")
#