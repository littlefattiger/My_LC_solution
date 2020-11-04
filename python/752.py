
# https://leetcode.com/problems/open-the-lock/
# it is a traditional BFS, using tuple in the deque, would be easy to do bfs, and remember that, for BFS if you do not want to have a new list, you need to use deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        
        queue = deque()
        queue.append(('0000', 0))
        seen = set()
        seen.add('0000')
        if '0000' in deadends_set:
            return -1
        while queue:
            string, step = queue.popleft()
            if string == target:
                return step
            for i in range(4):
                c = int(string[i])
                for add in [1, -1]:
                    nc = (c + add)%10
                    n_string = string[:i] + str(nc) + string[i+1:]
                    if n_string not in deadends_set and n_string not in seen:
                        seen.add(n_string)
                        queue.append((n_string, step + 1))
                             
        return -1
