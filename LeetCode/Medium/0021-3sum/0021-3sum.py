class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 배열을 오름차순으로 정렬
        result = []

        for i in range(len(nums) - 2):
            # 중복되는 값을 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i+1, len(nums)-1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0 :
                    result.append([nums[i],nums[left],nums[right]])

                    while left<right and nums[left]==nums[left+1]:
                        left += 1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1

                    left+=1
                    right-=1
                
                elif total < 0 :
                    left+=1
                else:
                    right-=1
        
        return result

