class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        n=len(nums)
        nums.sort()
        for pivot in range(n-2):
            if pivot>0 and nums[pivot]==nums[pivot-1]:
                continue

            left=pivot+1
            right=n-1
            while left<right:
                three_sum=nums[pivot]+nums[left]+nums[right]
                if three_sum<0:
                    left+=1
                elif three_sum>0:
                    right-=1
                else:
                    answer.append([nums[pivot],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
    
        return answer

                  
