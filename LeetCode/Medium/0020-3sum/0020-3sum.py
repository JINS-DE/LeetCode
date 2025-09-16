"""
정렬 후 고정된 nums[i] 기준으로 투 포인터 방식으로 3sum 구하기
3sum = nums[i] + nums[j] + nums[k]
- 3sum == 0 인 경우 j++ , k--
- 3sum > 0 인 경우 k--
- 3sum < 0 인 경우 j++

중복된 값 건너뛰기

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []
        for i in range(n-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            j = i+1
            k= n-1

            while j<k:
                total = nums[i] + nums[j] + nums[k]
                if total==0:
                    answer.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while k>i and nums[k]==nums[k+1]:
                        k-=1
                elif total < 0:
                    j+=1
                else:
                    k-=1
        return answer

                

        