# hash 방식
# key : target-num, value : index
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,num in enumerate(nums):
            if num in hash:
                return [hash[num],i]
            else:
                hash[target-num]=i

