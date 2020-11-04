# https://leetcode.com/problems/sliding-puzzle/
# a very straightforawrd BFS method, rememebr to do deepcopy, otherwise the array would change even you just copy

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def combine(board):
            return ''.join( str(i) for i in   (board[0] + board[1]))
        def reverse_combine(s):
            r = [[0,0,0],[0,0,0]]
            
            for i in range(2):
                for j in range(3):
                    r[i][j] = int(s[i *3 + j])
            return r
            
        target = '123450'
        current = combine(board)
         
        seen = set()
        seen.add(current)
        queue = deque()
        queue.append((current, 0))
         
        while queue:
            #print(queue)
            string, step = queue.popleft()
            if string == target:
                return step
            zero = string.index('0')
            zero_r = zero //3
            zero_c = zero % 3
            
            string_array = reverse_combine(string)
            for dx, dy in [(0,1), (-1,0),(1,0),(0,-1)]:
                nx = zero_r + dx
                ny = zero_c + dy
                if nx < 0 or ny < 0 or nx > 1 or ny > 2:
                    continue
                string_array2 =  deepcopy(string_array)
                string_array2[zero_r][zero_c], string_array2[nx][ny] = string_array2[nx][ny], string_array2[zero_r][zero_c]
                string_new = combine(string_array2)
                if string_new not in seen:
                    seen.add(string_new)
                    queue.append((string_new, step + 1))
        
        return -1
            
            
        
