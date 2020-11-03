 #https://leetcode.com/problems/two-sum/submissions/
 # very easy two sum and it test hash table, itetation, slide window
 class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()
        for i,v in enumerate(nums):
            if target - v in h:
                return [h[target - v], i]
            else:
                h[v ] = i
