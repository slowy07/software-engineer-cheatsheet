class ProblemSolve:
    def find_median_sorted_array(self, nums1: List[int], nums2: List[int]) -> float:
        merge_list = nums1 + nums2
        merge_list.sort()
        length = len(merge_list)
        if length % 2:
            return merge_list[int((length + 1) / 2) - 1]
        return (
            merge_list[int(length / 2) - 1] + merge_list[int((length / 2) + 1) - 1]
        ) / 2
