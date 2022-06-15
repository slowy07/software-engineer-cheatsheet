# add digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

```
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
```

```
Input: num = 0
Output: 0
```

```
constraint 0 <= num <= 231 - 1
```

```python
class ProblemSolve:
    def add_digit(self, num: int) -> int:
        while num > 9:
            sum = 0
            while num:
                sum += num % 10
                num = num // 10
            
            num = sum
        
        return num
```