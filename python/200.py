# simple use dfs to count number of islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0 :
            return 0
        n = len(grid[0])
        def helper(grid,x,y,m,n):
            if x < 0 or y < 0 or x >=m or y >= n or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            helper(grid,x + 1,y,m,n)
            helper(grid,x - 1,y,m,n)
            helper(grid,x,y + 1,m,n)
            helper(grid,x,y - 1,m,n)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                helper(grid,i,j,m,n)
                res += 1
        return res
        
