# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

# The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        def dfs(x, y, grid, visited, height):
            m = len(grid)
            n = len(grid[0])
            if grid[x][y] > height:
                return False
            if x == m - 1 and y == n - 1:
                return True
            visited.add((x, y))
            df = [(-1,0), (1, 0), (0,1), (0,-1)]
            for dx, dy in df:
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or (new_x, new_y) in visited or grid[new_x][new_y] > height:
                    continue
                if dfs(new_x, new_y, grid, visited, height):
                    return True
            return False
        l = 0
        r = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                r = max(r, grid[i][j])
        r += 1
        while l < r:
            m = (l + r)//2
            if dfs(0, 0, grid, set(), m):
                r = m
            else:
                l = m + 1
        return l
