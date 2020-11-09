# https://leetcode.com/problems/shortest-path-to-get-all-keys/
# the problem is very straightforward, just use a bfs method, and use bit mask to store available keys. The important thing to remember is that, in your each move, you need to store the current key, incase you change it in your previous move.
# use location and keys as the indicator whether you are in this position before
# copy the key value in every steps
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        keys = [-1] * 6
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i,j)
                if grid[i][j].isalpha():
                    keys[ord(grid[i][j].lower()) - ord('a')] = 1
        tot_keys = sum(1 for i in keys if i != -1 )
        target = (1 << tot_keys) - 1
        #print(tot_keys, target)
        seen = set()
        seen.add((start[0], start[1], 0))
        queue = deque()
        queue.append((start[0], start[1], 0, 0))
        while queue:
            #print(queue)
            x,y, keys, steps = queue.popleft()
            
            if keys == target:
                return steps
            for dx, dy in [(-1,0), (1,0),(0,1),(0,-1)]:
                nx = dx + x
                ny = dy + y
                new_key = keys
                if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] == '#' :
                    continue
                char = grid[nx][ny]   
                if ord(char) >= ord('A') and ord(char) <= ord('F') and not ((1<< (ord(char) - ord('A') )) & keys):
                    continue
                if ord(char) >= ord('a') and ord(char) <= ord('f'):
                    new_key  |=   (1<< (ord(char) - ord('a') ))
                if (nx,ny, keys) not in seen:
                    queue.append((nx,ny, new_key, steps + 1))
                    seen.add((nx,ny, new_key))
        return -1
