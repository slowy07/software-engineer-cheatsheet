class ProblemSolve:
    def remove_duplicate(self, nums: List[int]) -> int:
        nums2 = list(set(nums))
        nums2.sort()
        for i in range(len(nums2)):
            nums[i] = num2[i]

        return len(nums2)
