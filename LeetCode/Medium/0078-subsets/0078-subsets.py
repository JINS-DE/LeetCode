class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        def backtrack(index,li):
            if index == len(nums):
                answer.append(li[:])
                return
            backtrack(index+1,li)
            
            li.append(nums[index])
            backtrack(index+1,li)
            li.pop()

        backtrack(0,[])
        return answer
