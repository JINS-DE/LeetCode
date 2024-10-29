# 바텀업 방식
class Solution:
    def climbStairs(self, n: int) -> int:
        dic={0:1,1:1}
        for n in range(2,n+1):
            dic[n] = dic[n-1]+dic[n-2]
        return dic[n]

# 메모이제이션 방식
class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {}
        def fibo(n):
            if n<=1:
                return 1
            if n in dic:
                return dic[n]
            dic[n] = fibo(n-1)+fibo(n-2)
            return dic[n]
        return fibo(n)