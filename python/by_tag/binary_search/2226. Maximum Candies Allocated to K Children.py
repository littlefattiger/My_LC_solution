# You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

# You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can take at most one pile of candies and some piles of candies may go unused.

# Return the maximum number of candies each child can get.

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 0
        r = max(candies) + 1
        while l < r:
            m = (l + r + 1) // 2
            temp_k = sum([candy// m for candy in candies])
            if sum([candy// m for candy in candies]) < k:
                r = m - 1
            else:
                l = m
        return l
