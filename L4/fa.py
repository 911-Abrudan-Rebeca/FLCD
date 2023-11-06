class FiniteAutomata:

    def __init__(self, Q, E, q0, F, S):
        self.Q = Q
        self.E = E
        self.q0 = q0
        self.F = F
        self.S = S

    @staticmethod
    def getLine(line):
        # Only get what comes after the '='
        return line.strip().split(' ')[2:]

    @staticmethod
    def validate(Q, E, q0, F, S):
        if q0 not in Q:
            return False
        for f in F:
            if f not in Q:
                return False
        for key in S.keys():
            state = key[0]
            symbol = key[1]
            if state not in Q:
                return False
            if symbol not in E:
                return False
            for dest in S[key]:
                if dest not in Q:
                    return False
        return True

    @staticmethod
    def readFromFile(file_name):
        with open(file_name) as file:
            Q = FiniteAutomata.getLine(file.readline())
            E = FiniteAutomata.getLine(file.readline())
            q0 = FiniteAutomata.getLine(file.readline())[0]  # Only get the letter
            F = FiniteAutomata.getLine(file.readline())

            file.readline()  # S =


