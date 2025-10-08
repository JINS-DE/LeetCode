"""
슬라이딩 윈도우 방식
- 투포인터 left, right
- s[right] 중복체크 -> set()
    - 중복이 없으면 set에 추가 및 right+1
    - 중복이 있으면 left+1, left의 set 원소 제거
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_size = len(s)
        left,right=0,0
        answer = 0 
        valid_check = set()

        while right < s_size:
            if s[right] not in valid_check:
                valid_check.add(s[right])
                answer=max(answer,right-left+1)
                right+=1
            else:
                valid_check.remove(s[left])
                left+=1
        
        return answer