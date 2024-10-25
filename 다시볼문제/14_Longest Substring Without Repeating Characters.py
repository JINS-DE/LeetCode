'''Sliding window O(N)'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_len = 0
        left = 0

        for right,st in enumerate(s):
            if st in used and left <= used[st]:
                left = used[st]+1
            else:
                max_len = max(max_len,right-left+1)
            used[st]=right
    
       
        return max_len

'''완탐 방식 O(N^2)'''
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_len = 0

#         for i in range(len(s)):
#             check_li = set()
#             for j in range(i,len(s)):
#                 if s[j] in check_li:
#                     break
#                 else:
#                     check_li.add(s[j])
#                     max_len = max(max_len, len(check_li))
        
#         return max_len