class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 해쉬 (딕셔너리 방식 O(n))
        dic = {}
        for i,val in enumerate(nums):
            comp_num = target-val
            if comp_num in dic:
                return [dic[comp_num],i]
            dic[val]=i
        
        # 완탐방식
        # n=len(nums)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
