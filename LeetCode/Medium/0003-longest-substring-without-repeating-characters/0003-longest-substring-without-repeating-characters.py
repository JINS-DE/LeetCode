class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        answer=0

        sets = set()
        while right < len(s):
            
            if s[right] not in sets:
                sets.add(s[right])
                answer=max(answer,right-left+1)
                right+=1
            else:
                sets.remove(s[left])
                left+=1
            
        return answer
