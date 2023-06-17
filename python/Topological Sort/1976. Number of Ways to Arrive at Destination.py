# There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

# A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

# The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

# Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        g = defaultdict(dict)
        for u, v, w in edges:
            g[u - 1][v-1] = w
            g[v - 1][u-1] = w
        shortest = [float("inf")] *n
        shortest[-1] = 0

        heap = []
        heapq.heappush(heap, (0, n - 1))
        while heap:
            dist, node = heappop(heap)
            for nei in g[node]:
                if shortest[node] + g[node][nei] < shortest[nei]:
                    shortest[nei] = shortest[node] + g[node][nei]
                    heapq.heappush(heap, (shortest[nei], nei))

        seen = set()
        cache_dict = {}
        def dfs(node,n):
            if node == n -1:
                return 1
            if node in cache_dict:
                return cache_dict[node]
            count = 0
            seen.add(node)
            for child in g[node]:
                if  shortest[child]< shortest[node] and child not in seen:
                    count += dfs(child, n)
            seen.discard(node)
            cache_dict[node] = count
            return count
        return dfs(0,n)%M
