# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
# remember to check whether this position is visited when we process the point, maybe it has been visited by other path, then we did not need to process this point.
# otherwise, it would TlE, double layer save. If it is there, do not add, and if it is there, do not process. Important pruning.
#Like 16, 17 is important
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        seen = set()
        queue = []
        heappush(queue,(0,0,0))
        direction = [(0,1), (0,-1),(1,0), (-1,0)]
        m = len(grid)
        n = len(grid[0])
        while queue:
            #print(queue)
            steps,x,y = heappop(queue)
            if (x, y ) in seen:
                continue
            seen.add( (x, y))
            if x == m - 1 and y == n - 1:
                return steps
            for i in range(4):
                dx, dy = direction[i]
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen:
                    continue
                if grid[x][y] == i + 1:
                    heappush(queue,( steps, nx,ny))
                else:
                    heappush(queue,( steps + 1, nx,ny))
        return - 1
