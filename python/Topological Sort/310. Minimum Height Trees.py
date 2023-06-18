# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = defaultdict(list)
        degree = [0] * n
        for f, t in edges:
            g[f].append(t)
            g[t].append(f)
            degree[f] += 1
            degree[t] += 1
        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        while queue and n > 2:
            size = len(queue)
            n -= size
            while size > 0:
                node = queue.popleft()
                size -= 1
                for nei in g[node]:
                    if degree[nei] > 1:
                        degree[nei] -= 1
                        if degree[nei] == 1:
                            queue.append(nei)
                    else:
                        continue
        ans = []
        while queue:
            ans.append(queue.pop())
        return ans
