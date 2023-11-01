from SymbolTable import ConstantsSymbolTable,IdentifiersSymbolTable

import re

class Scanner:

    def __init__(self, filepath):
        """
        Initializes an instance of the Scanner class with the provided file path and initializes data structures and
        variables to be used during lexical analysis.
        :param filepath: The path to the source code file to be analyzed.
        """
        self.operators = ["+", "-", "*", "/", "==", "<=", ">=", "!=", "<", ">", "=","%"]
        self.separators = ["(", ")", "{", "}", ",", ";", ":", " ", "\n", "\""]
        self.reservedWords = ["var", "int", "str", "read", "print", "if", "else", "do", "while"]
        self.constantST = ConstantsSymbolTable(200)
        self.identifiersST = IdentifiersSymbolTable(200)
        self.pifOutput = []
        self.filePath = filepath

    def readFile(self):
        """
        Reads the content of the source code file line by line and returns it as a single string.
        :return: A single string containing the content of the source code file.
        """
        fileContent = ""

        with open(self.filePath, 'r') as file:
           for line in file:
               fileContent = fileContent + line.strip() + "\n"  # Add file lines to fileContent; whitespaces removed

        return fileContent

    def getProgramTokens(self):
        """
        Takes the source code, identifies and extracts individual tokens (keywords, identifiers, operators, constants, and separators)
        :return: A list of tokens extracted from the source code.
        """
        try:
            content = self.readFile()
            tokens = []
            local_word = ""  # temporary string
            in_quoted_string = False  # part of "" or no

            # iterates character by character
            for char in content:
                if in_quoted_string:
                    local_word += char
                    if char == '"':
                        in_quoted_string = False

                elif char not in self.operators and char not in self.separators:
                    local_word += char  # If char is not in the operators or separators, we add it to form the word

                else:  # if operator or separator => end of current token
                    if local_word:
                        tokens.append(local_word)  # add to tokens
                        local_word = ""  # reset to empty
                    if char == '"':  # start of str
                        local_word = '"'
                        in_quoted_string = True
                    elif char.strip() or char in self.operators or char in self.separators:  # empty local_word, or space, or operator, or separator
                        tokens.append(char)

            # (if exists) add remaining word
            if local_word:
                tokens.append(local_word)

            return tokens

        except FileNotFoundError as e:
            print(e)

        return None

    def scan(self):
        """
        Lexical analysis
        Validates the tokens, creates a PIF and checks for lexical errors.
        :return:
        """
        tokens = self.getProgramTokens()  # list of tokens
        counter = 0
        lexical_error_exists = False  # flag to track lexical errors
        identifier_positions = {}  # dictionary to store positions of identifiers
        constant_positions = {}  # dictionary to store positions of constants
        identifier_counter = 0 # current count
        constant_counter = 0

        if tokens is None:
            return

        for t in tokens:
            token = t

            if token in self.reservedWords:
                self.pifOutput.append([token, -1])
            elif token in self.operators:
                self.pifOutput.append([token, -1])
            elif token in self.separators:
                self.pifOutput.append([token, -1])

            elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):  # Check for valid identifier
                if token not in identifier_positions:
                    identifier_counter += 1
                    identifier_positions[token] = identifier_counter
                    if self.identifiersST.search(token) == -2:  # not in symbol table
                        self.identifiersST.insert(token, self.identifiersST.__len__())
                self.pifOutput.append(['IDENTIFIER', identifier_positions[token]])
            elif re.match(r'^(0|[-+]?[1-9][0-9]*|\'[1-9]\'|\'[a-zA-Z]\'|\"[0-9]*[a-zA-Z ]*\"|".*\s*")$',token):  # Check for valid constant
                if token not in constant_positions:
                    constant_counter += 1
                    constant_positions[token] = constant_counter
                    if self.constantST.search(token) == -2:  # not in the symbol table
                        self.constantST.insert(token, self.constantST.__len__())
                self.pifOutput.append(['CONSTANT', constant_positions[token]])

            else:
                print(f"Invalid token: {token} on line {counter}")
                lexical_error_exists = True

            if token == "\n":  # line number
                counter += 1

        if not lexical_error_exists:
            print("Program is lexically correct!")






    def find_token_index(self, target_token):
        """
        Find the index of a target_token in 'token.in' file.
        :param target_token: The token to find in 'token.in'.
        :return: The index of the target_token if found; otherwise, None.
        """
        with open('token.in', 'r') as file:
            for line in file:
                line = line.strip()
                if target_token in line:
                    index = line.split()
                    return index[0]

    def get_pif(self):
        """
        Get the Program Internal Form (PIF).
        :return: PIF as a list of token-index pairs
        """
        return self.pifOutput

    def get_constantST(self):
        return self.constantST

    def get_identifiersST(self):
        return self.identifiersST

