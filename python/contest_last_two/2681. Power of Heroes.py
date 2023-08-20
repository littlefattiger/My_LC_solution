# 贡献
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        s, res, M = 0, 0, 10**9 + 7
        for num in nums:
            res  += num**2 *(num + s)
            s = 2*s + num
        return res%M