# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

# DFS
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def dfs(x, y, grid, visited, height):
            m = len(grid)
            n = len(grid[0])

            if x == m - 1 and y == n - 1:
                return True
            visited.add((x, y))
            df = [(-1,0), (1, 0), (0,1), (0,-1)]
            for dx, dy in df:
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or (new_x, new_y) in visited or abs(grid[new_x][new_y] - grid[x][y]) > height:
                    continue
                if dfs(new_x, new_y, grid, visited, height):
                    return True
            return False
        l = 0
        r = 10 ** 7
        while l < r:
            m = (l + r) //2
            if dfs(0, 0, heights, set(), m):
                r = m
            else:
                l = m + 1
        return l
      
# BFS
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        
        if not m :
            return 0
        n = len(heights[0])
        
        heap = [(0,0,0)]
        visit = set()
        res = 0
        while heap:
            distance,x,y = heappop(heap)
            visit.add((x,y))
            res = max(res, distance)
            if x == m - 1 and y == n - 1:
                return res
            for dx, dy in [(-1,0),( 1,0), (0,1), (0,-1)  ]:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < m and ny >= 0 and ny < n and (nx,ny) not in visit:
                    nd =  abs(heights[nx][ny] - heights[x][y])
                    heappush(heap, (nd, nx,ny))       
