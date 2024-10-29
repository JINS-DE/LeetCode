
# # 재귀 함수로 풀기
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def find_palindrome(left: int, right: int) -> str:
#             # 기본 종료 조건
#             if left < 0 or right >= len(s) or s[left] != s[right]:
#                 return s[ left+1 : right ]  # 가장 최근의 팰린드롬 반환

#             # 양 끝을 확장하며 팰린드롬 확인
#             return find_palindrome(left - 1, right + 1)
        
#         longest = ""
#         for i in range(len(s)):
#             # 홀수 길이의 팰린드롬 (한 문자 중심)
#             palindrome1 = find_palindrome(i, i)
#             # 짝수 길이의 팰린드롬 (두 문자 중심)
#             palindrome2 = find_palindrome(i, i + 1)

#             # 가장 긴 팰린드롬을 갱신
#             longest = max(longest, palindrome1, palindrome2, key=len)

#         return longest

# 바텀업
def longest_palindrome_bottomup(s: str) -> str:
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

# 탑다운
def longest_palindrome_topdown(s: str) -> str:
    n = len(s)
    is_palindrome = [[None] * n for _ in range(n)]

    def is_palindrome_recursive(left: int, right: int) -> bool:
        # 이미 계산된 결과가 있으면 사용
        if is_palindrome[left][right] is not None:
            return is_palindrome[left][right]
        # 문자열이 팰린드롬인지 확인
        if left >= right:
            result = True
        else:
            result = (s[left] == s[right]) and is_palindrome_recursive(left + 1, right - 1)
        
        # 결과를 메모이제이션
        is_palindrome[left][right] = result
        return result

    longest = ""
    for i in range(n):
        for j in range(i, n):
            if is_palindrome_recursive(i, j) and (j - i + 1) > len(longest):
                longest = s[i:j + 1]

    return longest

# 예시
print(longest_palindrome_topdown("babad"))  # "bab" 또는 "aba"
print(longest_palindrome_topdown("cbbd"))   # "bb"

# # 테스트용
# def longest_palindrome_recursive(s: str) -> str:
#     def find_palindrome(left: int, right: int) -> str:
#         # 기본 종료 조건
#         if left < 0 or right >= len(s) or s[left] != s[right]:
#             return s[left + 1:right]  # 가장 최근의 팰린드롬 반환

#         # 양 끝을 확장하며 팰린드롬 확인
#         return find_palindrome(left - 1, right + 1)
    
#     longest = ""
#     for i in range(len(s)):
#         # 홀수 길이의 팰린드롬 (한 문자 중심)
#         palindrome1 = find_palindrome(i, i)
#         # 짝수 길이의 팰린드롬 (두 문자 중심)
#         palindrome2 = find_palindrome(i, i + 1)

#         # 가장 긴 팰린드롬을 갱신
#         longest = max(longest, palindrome1, palindrome2, key=len)

#     return longest
