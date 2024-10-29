class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)
        for i in nums:
            if i != min_ and i!=max_:
                return i
        return -1