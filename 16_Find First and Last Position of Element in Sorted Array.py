from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeftIndex(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left  
            
        def findRightIndex(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if  nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        leftIndex = findLeftIndex(nums, target)
        rightIndex = findRightIndex(nums, target)
        
        if leftIndex <= rightIndex and leftIndex < len(nums) and nums[leftIndex] == target:
            return [leftIndex, rightIndex]
        return [-1, -1]
        

# 테스트 코드
nums = [5,6,7,7,8,8,10]
k=8
solution = Solution()  # Solution 클래스 인스턴스 생성
result = solution.searchRange(nums,k)  # 함수 호출
print("answer :",result)  # 결과 출력