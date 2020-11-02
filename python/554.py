# https://leetcode.com/problems/brick-wall/
# the place with least overlap is the place with the most ending  -> accumulate the number in each row

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = Counter()
        max_num = 0
        for i in range(len(wall)):
            tot = 0
            for j in range( len(wall[i]) - 1):
                tot += wall[i][j]
                d[tot] += 1
                max_num = max(max_num, d[tot])
        return len(wall) - max_num
