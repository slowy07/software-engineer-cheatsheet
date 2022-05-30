# Letter combinations of a phone number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![phone](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

```python
class ProblemSolve:
    def letter_combination(self, digits) -> List[str]:
        res = []
        
        d={'2':'abc',
           '3':'def',
           '4':'ghi',
           '5':'jkl',
           '6':'mno',
           '7':'pqrs',
           '8':'tuv',
           '9':'wxyz'}

        def backtrack(i, curr):
            
            if len(digits)==len(curr):
                res.append(curr)
                return
            
            for j in d[digits[i]]:
                backtrack(i + 1, curr+j)
        
        
        if digits:
            backtrack(0, "")
        
        return res
```