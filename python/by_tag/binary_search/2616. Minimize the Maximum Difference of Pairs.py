# You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        n = len(nums)
        while left < right:
            m = (left + right)//2
            k = 0
            i = 1
            while i < n:
                if nums[i] - nums[i-1] <= m:
                    k += 1
                    i += 1
                i += 1
            if k >= p:
                right = m
            else:
                left = m + 1
        return left
