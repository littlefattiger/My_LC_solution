# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        in_degree = [0] * numCourses
        for post, pre in prerequisites:
            graph[pre].append(post)
            in_degree[post] += 1
        queue = collections.deque()
        for i in range(numCourses):
            if not in_degree[i]:
                queue.append(i)
        ans = []
        while queue:
            cur_node = queue.popleft()
            ans.append(cur_node)
            for child in graph[cur_node]:
                in_degree[child] -= 1
                if not in_degree[child]:
                    queue.append(child)
        if len(ans) < numCourses:
            return []
        else:
            return ans
