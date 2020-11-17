# pay attention to k =0, this is a corner case
# https://leetcode.com/problems/k-diff-pairs-in-an-array/
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = collections.Counter(nums)
         
        result = 0
        #print(count)
        for i in count:
            if k ==0 and count[i] > 1:
                result += 1
            elif k > 0 and i +k in count:
                result += 1
        return result
