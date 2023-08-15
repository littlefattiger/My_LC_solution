class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        m = 10 ** 9 + 7
        last_one = -1
        ans = -1
        for i, num in enumerate(nums):
            if num == 1 and last_one == -1:
                last_one = i
                ans = 1
            elif num == 1:
                ans *= i - last_one
                last_one = i
        if ans == -1:
            return 0
        return ans % m