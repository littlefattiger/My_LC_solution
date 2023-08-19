class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        d = [0] * (n + 1)
        cur_d = 0

        for i, num in enumerate(nums):
            cur_d += d[i]
            num += cur_d
            if num == 0:
                continue
            elif num < 0:
                return False
            if i + k > n:
                return False
            cur_d -= num
            d[i + k] += num
        return True

# Elegent one

class Solution:
    def checkArray(self, A: List[int], k: int) -> bool:
        cur = 0
        for i, a in enumerate(A):
            if a < cur:
                return False
            A[i] -= cur
            cur += A[i]
            # cur2 = a
            if i >= k - 1:
                cur -= A[i - k + 1]
        return cur == 0