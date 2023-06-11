# You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

# The chosen integers have to be in the range [1, n].
# Each integer can be chosen at most once.
# The chosen integers should not be in the array banned.
# The sum of the chosen integers should not exceed maxSum.
# Return the maximum number of integers you can choose following the mentioned rules.
# Greed
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        ban_set = set(banned)
        tot = 0
        count = 0
        for i in range(1, n  + 1):
            if i not in ban_set and tot + i <= maxSum:
                tot += i
                count += 1
        return count
