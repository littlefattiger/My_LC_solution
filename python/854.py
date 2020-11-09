# https://leetcode.com/problems/k-similar-strings/
# naive method would TLE, we need to swap only not equal position, and after swap we can have this position filled, this pruning is great.

class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        seen = set()
        seen.add(A)
        queue = deque()
        queue.append((A, 0))
        n = len(A)
        if len(A) != len(B):
            return -1
        if Counter(A) != Counter(B):
            return -1
        while queue:
            current_node, step = queue.popleft()
            if current_node == B:
                return step
            i = 0
            while i < n and current_node[i] == B[i]:
                i += 1
            
            for j in range(i + 1, n):
                if current_node[j] == B[j] or current_node[j] != B[i]:
                        continue
                new_node = current_node[:i] + current_node[j] + current_node[i + 1 :j] + current_node[i] + current_node[j + 1 :]
                if new_node not in seen:
                    seen.add(new_node)
                    queue.append((new_node, step + 1))
        return -1
            
