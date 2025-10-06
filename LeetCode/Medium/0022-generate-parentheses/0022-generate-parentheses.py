class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer=[]
        def recur(left,right,st):
            if n*2==len(st):
                answer.append(st)
                return
            
            if  left<n :
                recur(left+1,right,st+'(')
            
            if right<left :
                recur(left,right+1,st+')')

        recur(0,0,"")

        return answer
            
