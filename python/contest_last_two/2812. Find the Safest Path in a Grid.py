import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    heapq.heappush(heap, (0, i, j))
        man_dist = [[float("inf") for _ in range(n)] for __ in range(n)]

        while heap:
            dist, x, y = heapq.heappop(heap)
            if man_dist[x][y] != float("inf"):
                continue
            man_dist[x][y] = dist

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                heapq.heappush(heap, (dist + 1, nx, ny))

        heap = [(-man_dist[0][0], 0, 0)]
        visit = set()
        while heap:
            dist, x, y = heapq.heappop(heap)

            if (x, y) in visit:
                continue
            visit.add((x, y))
            if x == n - 1 and y == n - 1:
                return min(- dist, man_dist[x][y])
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                heapq.heappush(heap, (- min(-dist, man_dist[nx][ny]), nx, ny))
        return -1