 # you can use prefix sum and index to get the answer, but I use sliding window in the contest
 class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = max(nums)
        start = 0
        d = defaultdict(int)
        accu = 0
        for i,v in enumerate(nums):
            accu += v
            d[v] += 1
            while d[v] > 1:
                d[nums[start]] -= 1
                accu -= nums[start]
                start += 1
            res = max(res, accu)
        return res
