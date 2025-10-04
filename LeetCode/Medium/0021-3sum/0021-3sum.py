class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sets = set()
        nums.sort()
        n=len(nums)
        for pivot in range(1,n):
            left = 0
            right = n-1
            while left<pivot and right>pivot:
                three_sum = nums[left] + nums[pivot] + nums[right]
                if three_sum<0:
                    left+=1
                elif three_sum>0:
                    right-=1
                else:
                    sets.add((nums[left],nums[pivot],nums[right]))
                    left+=1
                    right-=1
        
        return list(map(list,sets))