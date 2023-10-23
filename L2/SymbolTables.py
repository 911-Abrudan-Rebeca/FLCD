from HashTable import HashTable


class SymbolTable:
    def __init__(self, size):
        """
        using 3 hash tables for int, str, identifier
        :param size: the size of the hash tables
        """
        self.int_hash_table = HashTable(size)
        self.str_hash_table = HashTable(size)
        self.identifier_hash_table = HashTable(size)

    def insert_integer(self, name, value):
        """
        insert int symbol
        :param name: the name of the int
        :param value: the value of the int
        :return: -
        """
        self.int_hash_table.insert(name, value)

    def insert_string(self, name, value):
        """
        insert str symbol
        :param name: the name of the int
        :param value: the value of the int
        :return: -
        """
        self.str_hash_table.insert(name, value)

    def insert_identifier(self, name, data):
        """
        insert identifier symbol
        :param name: the name
        :param data: additional data for the identifier (type, val)
        :return: -
        """
        self.identifier_hash_table.insert(name, data)

    def get_integer(self, name):
        """
        retrive the val for a given int symbol
        :param name: the name
        :return: the value, or none if the symbol not found
        """
        return self.int_hash_table.get(name)

    def get_string(self, name):
        """
        retrive the val for a given str symbol
        :param name: the name
        :return: the value, or none if the symbol not found
        """
        return self.str_hash_table.get(name)

    def get_identifier(self, name):
        """
        retrive additional data for a given identifier symbol
        :param name: the name
        :return: the data, or none if the symbol not found
        """
        return self.identifier_hash_table.get(name)

    def delete_integer(self, name):
        """
        delete int symbol
        :param name: the name
        :return: the val deleted, or none
        """
        return self.int_hash_table.delete(name)

    def delete_string(self, name):
        """
        delete str symbol
        :param name: the name
        :return: the val deleted, or none
        """
        return self.str_hash_table.delete(name)

    def delete_identifier(self, name):
        """
        delete identifier symbol
        :param name: the name
        :return: the val deleted, or none
        """
        return self.identifier_hash_table.delete(name)


# Creating a SymbolTable
symbol_table = SymbolTable(size=5)

# Inserting an integer symbol
symbol_table.insert_integer("count", 10)

# Inserting a string symbol
symbol_table.insert_string("name", "John")

# Inserting an identifier symbol
symbol_table.insert_identifier("x", {'type': 'int', 'value': 42})

# Retrieving symbols
print(symbol_table.get_integer("count"))  # Should print 10
print(symbol_table.get_string("name"))    # Should print "John"
print(symbol_table.get_identifier("x"))    # Should print {'type': 'int', 'value': 42}

# Deleting symbols
symbol_table.delete_integer("count")
symbol_table.delete_string("name")
symbol_table.delete_identifier("x")
