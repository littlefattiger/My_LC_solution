class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        n = len(prices)
        max_k = k
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
        for i in range(0, n):
            for k in range(max_k, 0, -1):
                if i == 0:
                    dp[i][k][1] = - prices[i]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[-1][max_k][0]