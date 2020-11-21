# if pass bounder, + 1, if it  is -1 return
# https://leetcode.com/problems/island-perimeter/
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        self.peri = 0
        def dfs(grid,sr, sc):
            if sr < 0 or sc < 0 or sr >= len(grid) or sc >= len(grid[0]) or grid[sr][sc] == 0:
                self.peri += 1
                return 
            if grid[sr][sc] == -1:
                return
            grid[sr][sc] = -1
            dfs(grid,sr + 1, sc)
            dfs(grid,sr - 1, sc)
            dfs(grid,sr , sc -1)
            dfs(grid,sr , sc + 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(grid,i, j )
                     
        print (self.peri)
        return self.peri
