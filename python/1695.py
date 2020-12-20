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

       
       #Prefix sum here
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = max(nums)
        m = defaultdict(int)
        presum = [0] + nums
        for i in range(len(nums)):
            presum[i + 1] = nums[i] + presum[i]
        last = 0
        for i,v in enumerate(nums):
            if v in m:
                
                last = max(last, m[v] + 1)
            res = max(res,presum[i + 1] -  presum[last])
            m[v] = i
        return res
