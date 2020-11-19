# used BIT, this tree is 1 based
# https://leetcode.com/problems/range-sum-query-mutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self._tree = FenwickTree (len(nums) )
        for i in range(1,len(nums) + 1):
            self._tree.update(i, nums[i - 1])
        

    def update(self, i: int, val: int) -> None:
        
        self._tree.update(i + 1, val - self.nums[i])
        self.nums[i] = val
         
            
        

    def sumRange(self, i: int, j: int) -> int:
        return self._tree.query(j +1) - self._tree.query(i)
        
class FenwickTree():
    
    def __init__(self, n):
        self.pre_sum = [0] * (1 + n)
        
    def update(self, i, delta):
        while i < len(self.pre_sum):
            self.pre_sum[i] += delta
            i += i & (-i)
    
    def query(self,i):
        s = 0
        while i >0:
            s += self.pre_sum[i]
            i -= i & (-i)
        
        return s
