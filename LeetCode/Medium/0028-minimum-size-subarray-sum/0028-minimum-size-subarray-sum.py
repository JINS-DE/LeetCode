class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum=0
        answer=float("inf")
        is_here = dict()
        for j,num in enumerate(nums):
            prefix_sum += num

            diff = prefix_sum - target

            if diff in is_here:
                answer=min(answer,j-is_here[diff])
            
            is_here[prefix_sum]=j
        
        return answer if answer!=float("inf") else 0


