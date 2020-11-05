# Yes, when you consider seen set, you need to consider both node and color, then you can go alternative
# https://leetcode.com/problems/shortest-path-with-alternating-colors/
# using python dict can make the code shorter
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph_red = defaultdict(list)
        graph_blue = defaultdict(list)
        for edge in red_edges:
            x, y = edge
            graph_red[x].append(y)
             
        for edge in blue_edges:
            x, y = edge
            graph_blue[x].append(y)
             
        res = [-1]*n
        queue = deque()
        seen = set()
        
        seen.add((0,1))
        seen.add((0,-1))
        queue.append((0,0,1))
        queue.append((0,0,-1))
        #print(red_edges)
        while queue:
            node, step, col = queue.popleft()
            if res[node] == -1 or step < res[node]:
                res[node] = step
            
            if col == 1:
                if node in graph_red:
                    for v in graph_red[node]:
                        if (v,-1) not in seen:
                            seen.add((v,-1))
                            queue.append((v, step + 1, -1))                
            if col == -1:
                if node in graph_blue:
                    for v in graph_blue[node]:
                        if (v,1) not in seen:
                            seen.add((v,1))
                            queue.append((v, step + 1, 1))
         
        return res
