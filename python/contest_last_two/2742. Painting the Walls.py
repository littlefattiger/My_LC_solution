# https://leetcode.com/problems/painting-the-walls/


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        @cache
        def helper(i, n):
            if n <= 0:
                return 0
            if i >= len(cost):
                return float("inf")
            notTake = helper(i + 1, n)
            take = cost[i] + helper(i + 1, n - time[i] - 1)
            return min(notTake, take)
        return helper(0, n)
# 0-1 backpack problem