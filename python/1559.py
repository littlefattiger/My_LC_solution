
// using a visit matrix to check visiting and visited
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        if m == 0 :
            return False
        n = len(grid[0])
        if not n:
            return False
        visit = [[0 for j in range(n)] for i in range(m)]
         
        def helper(grid,x,y,m,n, original_x, original_y):
            if x < 0 or y < 0 or x >=m or y >= n  :
                return False
            if visit[x][y] == 1:
                return True
            if visit[x][y] == 2:
                return False
            visit[x][y] = 1
             
            for dx, dy in [(0,1), (0, -1), (1,0),(-1,0)]:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >=m or ny >= n  or (nx == original_x and original_y == ny) or grid[nx][ny] != grid[x][y]  :
                    
                    continue
                if helper(grid,nx,ny,m,n, x, y):
                    return True
            visit[x][y] = 2
            return False
        
        for i in range(m):
            for j in range(n):
                if not visit[i][j] and helper(grid,i,j,m,n, -1, -1):
                    return True
        return False
            
            
                
        
