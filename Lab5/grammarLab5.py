class Grammar:
    def __init__(self):
        self.nonterminals = set()
        self.terminals = set()
        self.productions = {}  # prod for each nonterminal
        self.start_symbol = None


    def read_grammar_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        # parse tood (form todo)


    def print_nonterminals(self):
        print("Nonterminals:", self.nonterminals)

    def print_terminals(self):
        print("Terminals:", self.terminals)

    def print_productions(self, nonterminal):
        if nonterminal in self.productions:
            print(f"Productions for {nonterminal}: {self.productions[nonterminal]}")
        else:
            print(f"No productions found for {nonterminal}")