class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        visited=[[0]*len(grid[0]) for _ in range(len(grid))]
        def dfs(r,c):
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=='1' and visited[nr][nc]==0:
                    visited[nr][nc]=1
                    dfs(nr,nc)
        answer=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and visited[i][j]==0 :
                    visited[i][j]=1
                    dfs(i,j)
                    answer+=1

        return answer