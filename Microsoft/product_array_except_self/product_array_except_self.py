class ProblemSolve:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N

        prefix = 1
        for i in range(N - 1):
            prefix = prefix * nums[i]
            res[i + 1] = prefix

        postfix = 1
        for i in range(N - 1, -1, -1):
            res[i] *= postfix
            postfix = postfix * nums[i]

        return res
