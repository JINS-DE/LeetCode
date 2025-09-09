# 1. 일단 li =[M,CM,XC]로 저장하고
# 2. 특징대로 빼기 더하기 해서 총합을 구하면됨

value={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

class Solution:
    def romanToInt(self, s: str) -> int:        
        # s[::-1] test해보자
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




        