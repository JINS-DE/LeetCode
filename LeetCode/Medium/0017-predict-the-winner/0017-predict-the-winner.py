class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        def solve(left,right):
            if left==right:
                return nums[left]
            
            pick_left = nums[left]-solve(left+1,right)
            pick_right = nums[right]-solve(left,right-1)

            return max(pick_left,pick_right)
        
        return solve(0,n-1) >= 0