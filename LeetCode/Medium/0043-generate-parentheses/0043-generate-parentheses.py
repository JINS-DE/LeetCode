class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs(left,right,st):
            if len(st) == n*2:
                answer.append(st)
                return
            
            if left < n:
                dfs(left+1,right,st+'(')
            
            if right < left:
                dfs(left,right+1,st+')')

        dfs(0,0,"")
        return answer