from bisect import bisect_left

# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        queue = []

        ans = float("inf")
        for i in range(x, n):
            num = nums[i]
            queue.append(num)
        queue.sort()
        for i in range(n - x):
            num = nums[i]
            potential_index = bisect_left(queue, num)
            if potential_index > 0:
                ans = min(ans, abs(num - queue[potential_index - 1]))
            if potential_index < len(queue):
                ans = min(ans, abs(num - queue[potential_index]))
            if potential_index < len(queue) - 1:
                ans = min(ans, abs(num - queue[potential_index + 1]))
            actual_val = nums[i + x]
            potential_index2 = bisect_left(queue, actual_val)
            del queue[potential_index2]
        return ans

# We can also try to insert value gradually then do binary search, but you need to use insort_left