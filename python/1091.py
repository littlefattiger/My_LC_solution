# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# nothing new, sumply BFS
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        seen = set()
        seen.add((0,0))
        if grid[0][0] == 1:
            return -1
        queue = deque()
        queue.append((0,0,1))
        
        while queue:
            x,y, step = queue.popleft()
            if x == m -1 and y == n -1:
                return step
            
            for dx,dy in [(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]:
                nx = x + dx
                ny = y + dy
                
                if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] == 1:
                    continue
                if (nx,ny) in seen:
                    continue
                queue.append((nx,ny, step + 1))
                seen.add((nx,ny))
            
        return -1
