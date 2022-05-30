# valid parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

```
Input: s = "()"
Output: true
```

```
Input: s = "()[]{}"
Output: true
```

```
Input: s = "(]"
Output: false
```

```python
class ProblemSolve:
    def __init__(self):
        self.stack = []
        self.dictu = {'{': '}', '[': ']', '(': ')'}

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
```