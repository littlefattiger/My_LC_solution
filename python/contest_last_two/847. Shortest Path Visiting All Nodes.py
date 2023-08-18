class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        visited = set()
        n = len(graph)
        goal = (1 << n) - 1
        queue = deque()
        ans = 0
        for i in range(n):
            pos = (i, 1 << i)
            queue.append(pos)
            visited.add(pos)
        while queue:
            size = len(queue)
            for _ in range(size):
                node, state = queue.popleft()
                if state == goal:
                    return ans
                for nei in graph[node]:

                    pos = (nei, (1 << nei) | state)
                    if pos not in visited:
                        queue.append(pos)
                        visited.add(pos)
            ans += 1
        return ans