class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=len(s)
        prev=0
        answer=0
        for i in range(n-1,-1,-1):
            now = hash[s[i]]
            if now < prev:
                answer-=now
            else:
                answer+=now
            prev = now
        return answer
        