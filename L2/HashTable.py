from collections.abc import Hashable
from typing import Any, List, Tuple

class HashTable:
    def __init__(self, size: int):
        """
        Initialize a hash table with a given size.
        :param size: The number of buckets.
        """
        self.size = size
        self.items: List[List[Any]] = [[] for _ in range(size)]

    def getSize(self) -> int:
        """
        Get the size of the hash table.
        :return: The size of the hash table.
        """
        return self.size

    def __hash(self, key: Hashable) -> int:
        """
        Private method to compute the hash value for a key.
        :param key: The key to hash.
        :return: The hash value.
        """
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            key_str = str(key)
            key_sum = sum(ord(char) for char in key_str)
            return key_sum % self.size
        else:
            raise ValueError("not str/int")

    def getHashValue(self, key: Hashable) -> int:
        """
        Get the hash value for a key.
        :param key: The key to hash.
        :return: The hash value.
        """
        return self.__hash(key)

    def add(self, key: Hashable) -> Tuple[int, int]:
        """
        Add a key to the hash table.
        :param key: The key to add.
        :return: A tuple representing the (bucket index, index within the bucket) where the key was added.
        :raises: Exception if the key is already in the table.
        """
        hashValue = self.getHashValue(key)
        if key not in self.items[hashValue]:
            self.items[hashValue].append(key)
            index = self.items[hashValue].index(key)
            return (hashValue, index)
        raise Exception(f"Key {key} is already in the table!")

    def contains(self, key: Hashable) -> bool:
        """
        Check if a key is in the hash table.
        :param key: The key to check.
        :return: True if the key exists in the hash table, otherwise False.
        """
        hashValue = self.getHashValue(key)
        return key in self.items[hashValue]

    def getPosition(self, key: Hashable) -> Tuple[int, int]:
        """
        Get the position of a key in the hash table.
        :param key: The key to find.
        :return: A tuple representing the (bucket index, index within the bucket) if the key is found.
                 (-1, -1) if the key is not found.
        """
        if self.contains(key):
            hashValue = self.getHashValue(key)
            index = self.items[hashValue].index(key)
            return (hashValue, index)
        return (-1, -1)

    def __str__(self) -> str:
        """
        Return a string representation of the hash table.
        :return: A string representation of the hash table.
        """

        return f"HashTable{{items={self.items}}}"

# Example usage
if __name__ == "__main__":
    hash_table = HashTable(10)
    hash_table.add(42)

    print(f"Position of 42 in the hash table: {hash_table.getPosition(42)}")
