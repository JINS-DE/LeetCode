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
        
