class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        comp = nums[0]
        index = 1

        for i in range(1,len(nums)):
            if comp!=nums[i]:
                nums[index] = nums[i]
                comp=nums[i]
                index+=1
        
        return index
        