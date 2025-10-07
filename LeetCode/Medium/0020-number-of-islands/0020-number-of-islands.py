from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        rows, cols = len(grid), len(grid[0])
        answer= 0 
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    answer+=1

                    # BFS
                    q = deque([(i,j)])
                    grid[i][j]='0'

                    while q:
                        r,c = q.popleft()

                        for k in range(4):
                            nr = r + dr[k]
                            nc = c + dc[k]

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                q.append((nr,nc))
                                grid[nr][nc]='0'
        return answer
