from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hash=defaultdict(list)
        answer=[]
        asc=ord('a')
        for i in range(2,10):
            if i<9 and not i==7:
                for _ in range(3):
                    hash[i].append(chr(asc))
                    asc+=1
            else:
                for _ in range(4):
                    hash[i].append(chr(asc))
                    asc+=1
        
        def backtrack(index, combi):
            if index == len(digits):    
                answer.append(combi)
                return
            for i in hash[int(digits[index])]:
                backtrack(index+1,combi+i)
        backtrack(0,'')
        return answer

