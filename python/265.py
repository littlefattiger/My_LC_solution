// use two number to record the smallest one
def minCost(costs):
	m = len(costs)
	if m == 0:
		return 0
	n = len(costs[0])
	if n == 0:
		return 0

	dp = [[0 for j in range(n)] for i in range(m)]
	min1 = -1
	min2 = -1
	for j in range(n):
		dp[0][j] = costs[0][j]
		if min1 < 0 or costs[0][j] < min1:
			min1 = costs[0][j]
			min2 = min1
		elif min2 < 0 or costs[0][j] < min2:
			min2 = costs[0][j]

	for i in range(1, m):
		last1 = min1
		last2 = min2
		min1 = -1
		min2 = -1 
		for j in range(n):
			if j == last1:
				dp[i][j] = dp[i -1][last2] + cost[i][j]
			else:
				dp[i][j] = dp[i -1][last1] + cost[i][j]
			if min1 < 0 or costs[i][j] < min1:
				min1 = costs[i][j]
				min2 = min1
			elif min2 < 0 or costs[i][j] < min2:
				min2 = costs[i][j]
	return min(dp[-1])
