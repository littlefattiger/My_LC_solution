from functools import cache
from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        m = 10 ** 9 + 7
        n = len(nums)

        @cache
        def helper(i, k, mask):
            if i == n:
                return 1
            ans = 0

            for j in range(n):
                if (mask & (1 << j)) == 0 and (i == 0 or nums[j] % nums[k] == 0 or nums[k] % nums[j] == 0):
                    ans += helper(i + 1, j, mask | (1 << j))
            return ans

        return helper(0, 0, 0) % m
