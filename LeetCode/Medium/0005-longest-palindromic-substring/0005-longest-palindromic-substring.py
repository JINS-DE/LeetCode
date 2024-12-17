class Solution:
    def longestPalindrome(self, s: str) -> str:

            n = len(s)
            if n == 0:
                return ""
            
            dp = [[False] * n for _ in range(n)]
            start = 0
            max_length = 1
            
            # 모든 한 글자 부분 문자열은 팰린드롬
            for i in range(n):
                dp[i][i] = True

            # 두 글자 부분 문자열 검사
            for i in range(n - 1):
                if s[i] == s[i + 1]:
                    dp[i][i + 1] = True
                    start = i
                    max_length = 2

            # 세 글자 이상 부분 문자열 검사
            for length in range(3, n + 1):  # 길이 3 이상
                for i in range(n - length + 1):
                    j = i + length - 1
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        start = i
                        max_length = length

            return s[start:start + max_length]
