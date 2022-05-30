# median of two sorted array

Given two sorted arrays ``nums1`` and ``nums2`` of size ``m`` and ``n`` respectively, return the median of the two sorted arrays.

The overall run time complexity should be ``O(log (m+n))``.

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

```python
class ProblemSolve:
    def find_median_sorted_array(self, nums1: List[int], nums2: List[int]) -> float:
        merge_list = nums1 + nums2
        merge_list.sort()
        length = len(merge_list)
        if length % 2:
            return merge_list[int((length + 1) / 2) - 1]
        return (merge_list[int(length / 2) - 1] + merge_list[int((length / 2) + 1) - 1]) / 2
```
        