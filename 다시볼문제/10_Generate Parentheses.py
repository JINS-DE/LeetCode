class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left,right,s):
            if n*2==len(s):
                answer.append(s)
                return

            if left < n :
                dfs(left+1, right, s+'(')
            
            if right < left :
                dfs(left,right+1,s+')')
        
        answer=[]
        dfs(0,0,'')
        return answer