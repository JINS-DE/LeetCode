class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        row = [0]*n
        col = [0]*m
        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    row[r]+=1
                    col[c]+=1
        answer=0
        for r in range(n):
            for c in range(m):
                if grid[r][c] and (row[r]>1 or col[c]>1):
                    answer+=1
        return answer