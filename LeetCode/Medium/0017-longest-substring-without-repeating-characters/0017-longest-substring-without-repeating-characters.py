"""
slide window 방식 
- 준비물 : left, right 포인터 / set , answer
- s[right] set에 없으면 right만 +1 및 answer 값 갱신, 있으면 left+1, right+1
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_ = set()
        answer=0
        left,right = 0,0
        while right<len(s):
            if s[right] not in set_:
                set_.add(s[right])
                answer=max(answer,right-left+1)
                right+=1
            else:
                set_.remove(s[left])
                left+=1

        return answer
            
        