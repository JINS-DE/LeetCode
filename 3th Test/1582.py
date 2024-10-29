class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        row = [0]*n
        col = [0]*m
        for r in range(n):
            for c in range(m):
                if mat[r][c]:
                    row[r]+=1
                    col[c]+=1
        answer=0
        for r in range(n):
            for c in range(m):
                if mat[r][c] and row[r]==1 and col[c]==1: # 1267문제에서 if문만 다름
                    answer+=1 
        return answer
    

# 3중 for문 비효율적
# class Solution:
#     def numSpecial(self, mat: List[List[int]]) -> int:
#         n=len(mat)
#         m=len(mat[0])
#         answer=0
#         for i in range(n):
#             for j in range(m):
#                 if mat[i][j] == 1:
#                     if sum(mat[i])==1 and sum(mat[k][j] for k in range(n))==1:
#                         answer+=1
#         return answer 