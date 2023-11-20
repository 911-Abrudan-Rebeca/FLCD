class Node:
    def __init__(self, key, value):
        """
        Initializes a Node in a linked list used for chaining in a hash table.
        :param key: The key associated with the node.
        :param value: The value associated with the node.
        """
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        """
        Initializes a hash table with chaining for handling key-value pairs.
        :param capacity: The initial capacity of the hash table.
        """
        self.capacity = capacity
        self.size = 1
        self.table = [None] * capacity

    def toString(self):
        """
        Returns a list of key-value pairs in the hash table as a human-readable string.
        :return: A list of key-value pairs represented as strings.
        """
        elements = []
        for index in range(self.capacity):
            current = self.table[index]
            while current:
                elements.append(f"{current.key}: {current.value}")
                current = current.next

        return elements

    def _hash(self, key):
        """
        Computes the hash value for a given key using a hash function.
        :param key: The key for which the hash value needs to be calculated.
        :return: The computed hash value, which is an index within the hash table's capacity.
        """
        return hash(key) % self.capacity

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table or updates the value if the key already exists.
        :param key: The key to insert or update.
        :param value: The value associated with the key.
        :return: None
        """
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        """
        Searches for a key in the hash table and returns its associated value if found.
        :param key: The key to search for.
        :return: The value associated with the key if found, or -2 if the key is not in the hash table.
        """
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return -2

    def getPositionPair(self, key):
        """
        Searches for a key in the hash table and returns a tuple with the index and position within the linked list.
        :param key: The key to search for.
        :return: A tuple containing the index and position of the key within the linked list if found, or -2 if not found.
        """
        index = self._hash(key)
        current = self.table[index]
        columnIndex = -1
        while current:
            columnIndex += 1
            if current.key == key:
                return (index ,columnIndex)
            current = current.next

        return -2

    def remove(self, key):
        """
        Removes a key-value pair from the hash table based on the provided key.
        :param key: The key to be removed.
        :return: None
        """
        index = self._hash(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def __len__(self):
        """
        Returns the current number of key-value pairs in the hash table.
        :return: The number of key-value pairs in the hash table.
        """
        return self.size

    def __contains__(self, key):
        """
        Checks if a key exists in the hash table.
        :param key: The key to check for existence.
        :return: True if the key exists, False if not.
        """
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def getValueIndex(self, elem):
        """
        Returns a tuple containing the index and position within the linked list of the specified element.
        :param elem: The element (key) to search for.
        :return: A tuple (index, position) if the element is found, or None if not found.
        """
        index = self._hash(elem)

        if self.table[index] is not None:
            current = self.table[index]
            position = 0

            while current:
                if current.key == elem:
                    return (index, position)
                current = current.next
                position += 1

        return None


# Symbol Tables
class ConstantsSymbolTable(HashTable):
    def insert(self, key, value):
        """
        Inserts a key-value pair into the constants symbol table.
        :param key: The key to insert.
        :param value: The value associated with the key.
        :return: None
        """
        super().insert(key, value)

    def contains(self, key):
        """
        Checks if a key exists in the constants symbol table.
        :param key: The key to check for existence.
        :return: True if the key exists, False if not.
        """
        try:
            super().search(key)
            return True
        except KeyError:
            return False

    def getValueIndex(self, key):
        """
        Returns a tuple containing the index and position within the linked list of the specified key in the constants symbol table.
        :param key: The key to search for.
        :return: A tuple (index, position) if the key is found, or None if the key is not in the symbol table.
        """
        return super().getValueIndex(key)

    def remove(self, key):
        """
        Removes a key-value pair from the constants symbol table based on the provided key.
        :param key: The key to be removed.
        :return: None
        """
        super().remove(key)

    def toString(self):
        return super(ConstantsSymbolTable, self).toString()


class IdentifiersSymbolTable(HashTable):
    def insert(self, key, value):
        """
        Inserts a key-value pair into the identifiers symbol table.
        :param key: The key to insert.
        :param value: The value associated with the key.
        :return: None
        """
        super().insert(key, value)

    def contains(self, key):
        """
        Checks if a key exists in the identifiers symbol table.
        :param key: The key to check for existence.
        :return: True if the key exists, False if not.
        """
        try:
            super().search(key)
            return True
        except KeyError:
            return False

    def getValueIndex(self, key):
        """
        Returns a tuple containing the index and position within the linked list of the specified key in the identifiers symbol table.
        :param key: The key to search for.
        :return: A tuple (index, position) if the key is found, or None if the key is not in the symbol table.
        """
        return super().getValueIndex(key)

    def remove(self, key):
        """
        Removes a key-value pair from the identifiers symbol table based on the provided key.
        :param key: The key to be removed.
        :return: None
        """
        super().remove(key)

    def toString(self):
        return super(IdentifiersSymbolTable, self).toString()
