class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        m = defaultdict(list)
        for s, e, g in offers:
            m[e].append((s, g))

        dp = [0] * (n + 1)
        for end in range(1, n + 1):
            dp[end] = dp[end - 1]
            for s, g in m[end - 1]:
                dp[end] = max(dp[end], dp[s] + g)

        return dp[-1]
