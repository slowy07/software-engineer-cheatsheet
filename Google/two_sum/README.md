# two sum

given an array of integer ``nums`` and an integer ``target``, return indices of the two numbers such that they add up to target

example

```
input: num = [2, 17, 11, 15]
target = 9
output: [0, 1]

explain: cause nums[0] + nums[1] == 9, and return [0, 1]
```
```
input: [3, 2, 4], target = 6
output = [1, 2]
```

```python
class SolveProblem:
  def two_sum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]

        if reamaining in seen:
          return[i, seen[remaining]]
```
