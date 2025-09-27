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
        n = len(digits)
        def backtrack(index,st):
            if index >= n:
                answer.append(st)
                return 

            alpa_li = hash[int(digits[index])]
            
            for c in alpa_li:
                st+=c
                backtrack(index+1,st)
                st = st[:len(st)-1]
        backtrack(0,"")
        

        return answer