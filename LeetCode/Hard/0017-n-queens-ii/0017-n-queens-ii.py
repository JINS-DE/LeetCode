class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0]*n for _ in range(n)]
        answer = 0
        col_visited = [0]*n
        left_diagonal = [0]*(2*n-1)
        right_diagonal = [0]*(2*n-1)
        def n_queens(row, col):
            if row==n:
                nonlocal answer
                answer+=1
                return

            for col in range(n):
                if col_visited[col]==0 and left_diagonal[row-col]==0 and right_diagonal[row+col]==0:
                    col_visited[col], left_diagonal[row-col], right_diagonal[row+col]= 1,1,1
                    n_queens(row+1,col)
                    col_visited[col], left_diagonal[row-col], right_diagonal[row+col]= 0,0,0

        n_queens(0,0)
        

        return answer
        
        
        