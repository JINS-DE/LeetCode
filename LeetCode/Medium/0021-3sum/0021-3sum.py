class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer=set()
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                three_sums = nums[i] + nums[j] + nums[k]
                if three_sums == 0:
                    answer.add((nums[i],nums[j],nums[k]))
                    j+=1
                elif three_sums < 0:
                    j+=1
                else:
                    k-=1

        return list(map(list, answer)) 


        