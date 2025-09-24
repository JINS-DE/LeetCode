"""
1. nums[::-1]
2. 

stack에는 2번째 크기

"""

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        num_3 = float("-inf")

        for num_1 in nums[::-1]:
            if num_1 < num_3:
                return True

            
            while stack and num_1 > stack[-1]:
                num_3 = stack.pop()
            
            stack.append(num_1)
        
        return False

        

