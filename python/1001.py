#https://leetcode.com/problems/grid-illumination/
# this is not a hard problem, it is a medium to easy problem. It is just use the hash table to record this row or column is illuminate

class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row = defaultdict(int)
        col = defaultdict(int)
        diag1 = defaultdict(int)
        diag2 = defaultdict(int)
        lamp_set = set()
        ans = []
        for x,y in lamps:
            lamp_set.add((x,y))
            row[x] += 1
            col[y] += 1
            diag1[x + y] += 1
            diag2[N + x - y] += 1
        for x, y in queries:
            if row[x] > 0 or col[y] > 0 or diag1[x + y] > 0 or diag2[N + x - y] > 0:
                ans.append(1)
            
            else:
                ans.append(0)
            
            for dx,dy in [(0,1), (0,-1),(-1,0),(1,0),(1,1),(-1,1),(1,-1),(-1,-1),(0,0)]:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if (nx,ny) in lamp_set:
                    lamp_set.remove((nx,ny))
                    row[nx] -= 1
                    col[ny] -= 1
                    diag1[nx + ny] -= 1
                    diag2[N + nx - ny] -= 1
        return ans
                
                
            
            
            
        
