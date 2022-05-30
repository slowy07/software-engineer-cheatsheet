class ProblemSolve:
    def letter_combination(self, digits) -> List[str]:
        res = []

        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curr):

            if len(digits) == len(curr):
                res.append(curr)
                return

            for j in d[digits[i]]:
                backtrack(i + 1, curr + j)

        if digits:
            backtrack(0, "")

        return res
