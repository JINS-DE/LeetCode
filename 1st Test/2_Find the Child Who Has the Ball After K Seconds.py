# 완탐
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        children = 0
        
        for i in range(k):
            if children == 0 :
                direction =True
            elif children == n-1:
                direction = False
            
            if direction :
                children +=1
            else:
                children -= 1

        return children

# 상수시간에 풀기    
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        if (k // (n-1)) % 2 == 0:
            return (k % (n - 1))
        else:
            return (n-1) - (k%(n-1))