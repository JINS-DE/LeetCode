class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[[0]*n for _ in range(n)]

        # 길이가 1인 구간의 최대값은 자기 자신
        for i in range(n):
            dp[i][i]=nums[i]
        
        for length in range(2,n+1):
            for left in range(n+1-length):
                right = left+length-1
                left_pick = nums[left] - dp[left+1][right]
                right_pick = nums[right] - dp[left][right-1]
                dp[left][right] = max(left_pick,right_pick)
        
        return dp[0][n-1] >= 0