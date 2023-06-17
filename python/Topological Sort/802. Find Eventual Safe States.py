# There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

# BFS
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out_degree = [0] * n
        edge_grapg = collections.defaultdict(list) 
        for i in range(n):
            for v in graph[i]:
                edge_grapg[v].append(i)
                out_degree[i] += 1
        queue = deque()
        ans = []
        for i in range(n):
            if out_degree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            ans.append(node)
            for v in edge_grapg[node]:
                out_degree[v] -= 1
                if out_degree[v] == 0:
                    queue.append(v)
        return sorted(ans)
