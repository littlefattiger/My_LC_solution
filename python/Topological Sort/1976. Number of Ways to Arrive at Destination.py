# You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

# You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

# Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:


        M = 10 ** 9 + 7
        g = defaultdict(list)
        for u, v, w in roads:
            g[u].append((v, w))
            g[v].append((u, w))
        ways = [0] * n
        shortest = [float("inf")] * n
        ways[0] = 1
        shortest[0] = 0
        heap = []
        heapq.heappush(heap, (0, 0))
        while heap:
            dist, node = heappop(heap)
            if dist > shortest[node]:
                continue
            for nei, weight in g[node]:
                if dist + weight < shortest[nei]:
                    shortest[nei] = dist + weight
                    heapq.heappush(heap, (shortest[nei], nei))
                    ways[nei] = ways[node]
                elif dist + weight == shortest[nei]:
                    ways[nei] += ways[node]

        return ways[-1]%M
