# generate parentheses

Given ``n`` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

```
Input: n = 1
Output: ["()"]
```

```python
class ProblemSolve:
    def generate_parentheses(self, n: int) -> List[str]:
        stack = []
        output = []

        def backtrack(opening, close):
            if len(stack) == 2*n:
                output.append("".join(stack))
                return
            
            if opening < n:
                stack.append("(")
                backtrack(opening + 1, closing)
                stack.pop()
            
            if close < opening:
                stack.append(")")
                backtrack(opening, close + 1)
                stack.pop()
            
        backtrac(0, 0)
        return ouput
```
