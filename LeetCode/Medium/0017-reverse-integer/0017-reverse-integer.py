class Solution:

    def reverse(self, x: int) -> int:
        if x==0:
            return 0 
        
        if x>0:
            answer = int(str(x)[::-1])
        else:
            answer = -int(str(x)[1:][::-1])

        if -2**31 > answer or 2**31-1 < answer or 
        return answer
