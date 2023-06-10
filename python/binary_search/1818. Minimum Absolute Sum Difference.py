# You are given two positive integer arrays nums1 and nums2, both of length n.

# The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).

# You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

# Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        M = 10 ** 9 + 7
        sorted_nums1 = sorted(nums1)
        gain = 0
        res = 0
        for i in range(n):
            origin = abs(nums1[i] - nums2[i])
            res += origin
            if gain < origin:
                pos = bisect_left(sorted_nums1, nums2[i])
                if pos < n:
                    gain = max(gain, origin - abs(nums2[i] - sorted_nums1[pos]))
                if pos != 0:
                    gain = max(gain, origin - abs(nums2[i] - sorted_nums1[pos - 1]))
            # print(res, gain)
        return (res - gain)%M
