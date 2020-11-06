# https://leetcode.com/problems/as-far-from-land-as-possible/
# Simply BFS, and step by step is manhatom distance
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        seen = set()
        queue = deque()
        N = len(grid)
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    seen.add((x,y))
                    queue.append((x,y,0))
        max_length = -1
        if len(queue) == N* N:
            return -1
        while queue:
            x,y, length = queue.popleft()
            max_length = max(max_length, length)
            #print(queue)
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= N or ny >= N or grid[nx][ny] == 1:
                    continue
                if (nx, ny) not in seen:
                    seen.add((nx, ny))
                    queue.append((nx, ny,length + 1))
             
        return max_length
