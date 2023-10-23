from SymbolTables import SymbolTable
import re

class Scanner:
    def __init__(self):
        # Initialize the Scanner with a symbol table and other attributes.
        self.symbol_table = SymbolTable(size=47)
        self.program = ""
        self.index = 0
        self.current_line = 1
        self.PIF = []

    def set_program(self, program):
        self.program = program

    def read_tokens(self):
        # Define the reserved words and operators
        reserved_words = ["var", "int", "str", "read", "print", "if", "else", "do", "while"]
        operators = ["+", "-", "*", "/", "==", "<", "<=", ">", ">=", "=", "!=", "%"]
        return reserved_words, operators

    def skip_spaces(self):
        # Skip over any whitespace
        while self.index < len(self.program) and self.program[self.index].isspace():
            if self.program[self.index] == '\n':
                self.current_line += 1
            self.index += 1

    def treat_string_constant(self):
        # Try to match a string constant pattern and insert it into the symbol table.
        string_constant_pattern = r'^"[a-zA-Z0-9_ ?:*^+=.!]*"'
        string_constant_match = re.match(string_constant_pattern, self.program[self.index:])
        if string_constant_match:
            string_constant = string_constant_match.group(0)
            position = self.symbol_table.insert_string(string_constant, string_constant)
            self.index += len(string_constant)
            return string_constant, position

    def treat_int_constant(self):
        # Try to match an integer constant pattern and insert it into the symbol table.
        int_constant_pattern = r'^[+-]?[1-9][0-9]*|0'
        int_constant_match = re.match(int_constant_pattern, self.program[self.index:])
        if int_constant_match:
            int_constant = int_constant_match.group(0)
            position = self.symbol_table.insert_integer(int_constant, int(int_constant))
            self.index += len(int_constant)
            return int_constant, position
