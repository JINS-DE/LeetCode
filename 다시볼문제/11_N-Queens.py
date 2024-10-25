from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(row):
            if row == n:  # 모든 행에 퀸을 다 놓았으면 결과 저장
                result.append(["".join(board[i]) for i in range(n)])
                return
            
            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue  # 대각선 또는 같은 열에 퀸이 있으면 스킵
                
                # 퀸 배치
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row + col)  # '/' 대각선
                diag2.add(row - col)  # '\' 대각선
                
                dfs(row + 1)  # 다음 행으로 이동
                
                # 퀸을 다시 빼고 다른 배치 탐색
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
        
        # 초기화
        result = []
        board = [["." for _ in range(n)] for _ in range(n)]  # 빈 체스판
        cols = set()   # 열 추적
        diag1 = set()  # '/' 대각선 추적
        diag2 = set()  # '\' 대각선 추적
        
        dfs(0)
        return result

solution = Solution()
result = solution.solveNQueens(4)
for board in result:
    for row in board:
        print(row)
    print()
