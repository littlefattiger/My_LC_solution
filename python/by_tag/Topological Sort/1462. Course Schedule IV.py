# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = defaultdict(list)
        in_degree = [0] * n
        ans_map = defaultdict(set)
        for f, t in prerequisites:
            g[t].append(f)  
        # print(g)
        def dfs(n ):
            if not g[n]:
                ans_map[n] = set()
                return set()
            if ans_map[n]:
                return ans_map[n]
            for child in g[n]:
                ans_map[n].add(child)
                ans_map[n].update(dfs(child))
            return ans_map[n]

        ans = []       
        for i in range(n):
            ans.append(sorted(list(dfs(i))))
        aa = []
        for a,b in queries:
            aa.append(a in ans_map[b])
        return aa
