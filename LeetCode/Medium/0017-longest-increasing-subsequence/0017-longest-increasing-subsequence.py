"""
dp 배열의 의미
dp[i] : i번째 반드시 포함해서 만들 수 있는 가장 긴 부분 수열의 길이

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)