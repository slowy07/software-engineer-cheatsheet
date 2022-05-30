class ProblemSolve:
    def __init__(self):
        self.stack = []
        self.dictu = {"{": "}", "[": "]", "(": ")"}

    def is_valid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        for i in s:
            if i in self.dictu.keys():
                self.stack.append(i)
            if i in self.dictu.values():
                if not self.stack:
                    return False
                elif i != self.dictu[self.stack.pop()]:
                    return False

        return self.stack == []
