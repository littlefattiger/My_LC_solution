# https://leetcode.com/problems/champagne-tower/
# if it is larger than 1, then pull to the next layer, iterate from 1 to query row
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for j in range(101)] for i in range(101)]
        dp[0][0] = poured
        for i in range(query_row + 1):
            for j in range( i + 1):
                if dp[i][j] > 1:
                    
                    dp[i + 1][j] += (dp[i][j] - 1)/2
                    dp[i + 1][j + 1] += (dp[i][j] - 1)/2
                    dp[i][j] = 1
        
        return dp[query_row][query_glass]
