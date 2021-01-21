// simple a dp solution with 3 different choice

def minCost(costs):
	n = len(costs)
	dp = [[0 for j in range(3)] for i in range(n)]
	dp[0][0] = cost[0][0]
	dp[0][1] = cost[0][1]
	dp[0][2] = cost[0][2]

	for i in range(1, n):
		dp[i][0]  = min(dp[i - 1][1],dp[i - 1][2] ) + costs[i][0]
		dp[i][1]  = min(dp[i - 1][0],dp[i - 1][2] ) + costs[i][1]
		dp[i][2]  = min(dp[i - 1][1],dp[i - 1][0] ) + costs[i][2]
	return min(dp[-1])
