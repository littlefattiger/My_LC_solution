# You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

# You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

# Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

# A node u is an ancestor of another node v if u can reach v via a set of edges.

# Topping sorting
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        in_degree = [0] * n
        for f, t in edges:
            g[f].append(t)
            in_degree[t] += 1
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        ans = [set() for i in range(n)]
        # print(g)
        # print(in_degree)
        while queue:
            node = queue.popleft()
            for child in g[node]:
                ans[child].add(node)
                if ans[node]:
                    for vv in ans[node]:
                        ans[child].add(vv)
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)
        return [sorted(list(x)) for x in ans]
# DFS
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        in_degree = [0] * n
        for f, t in edges:
            g[t].append(f)
            
        ans_map = defaultdict(set)
        # print(g)
        def dfs(n ):
            if not g[n]:
                ans_map[n] = set()
                return set()
            if ans_map[n]:
                return ans_map[n]
            for child in g[n]:
                ans_map[n].add(child)
                ans_map[n] = ans_map[n].union(dfs(child))
            return ans_map[n]
        ans = []       
        for i in range(n):
            ans.append(sorted(list(dfs(i))))
        return ans
