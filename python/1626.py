#https://leetcode.com/problems/best-team-with-no-conflicts/
#fix one position, and find longest increase subsequence

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pp = []
        for i in range(len(scores)):
            pp.append((ages[i], scores[i]))
        pp.sort()
        n = len(scores)
        dp = [0 for i in range(n )]
        dp[0] = pp[0][1]
        
        for i in range(1, n):
            dp[i] = pp[i][1]
            for j in range(i):
                if pp[i][1] >= pp[j][1]:
                    dp[i] = max(dp[i], dp[j] + pp[i][1])
                 
        
        return max(dp)
