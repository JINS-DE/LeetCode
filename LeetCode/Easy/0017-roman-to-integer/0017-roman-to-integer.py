class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        answer = 0
        before = 0
        for ch in s[::-1]:
            cur=value[ch]
            if cur < before:
                answer-=cur
            else:
                answer+=cur
            before = cur
        return answer
        