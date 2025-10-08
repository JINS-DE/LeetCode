"""
슬라이딩 윈도우 방식
- 투포인터 left, right
- s[right] 중복체크 -> set()
    - 중복이 없으면 set에 추가 및 right+1
    - 중복이 있으면 left+1, left의 set 원소 제거

최적화 방식
- 딕셔너리를 활용해서 중복 발견시 해당 인덱스로 jump
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 최적화 방식
        n = len(s)
        left = 0
        answer = 0
        valid = dict()
        
        for right, char in enumerate(s):
            if char in valid and valid[char] >= left:
                left=valid[char]+1

            valid[char]=right
            answer = max(answer,right-left+1)

        return answer 
        # 이전 방식
        # s_size = len(s)
        # left,right=0,0
        # answer = 0 
        # valid_check = set()

        # while right < s_size:
        #     if s[right] not in valid_check:
        #         valid_check.add(s[right])
        #         answer=max(answer,right-left+1)
        #         right+=1
        #     else:
        #         valid_check.remove(s[left])
        #         left+=1
        
        # return answer