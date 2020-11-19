# https://leetcode.com/problems/create-sorted-array-through-instructions/
# this question is a template for BIT, here we use max(A) array, we just simply calculate how many number larget then him
# bit is 1 base, then means get(a) would get the sum until a, hense we use min(get(a-1), i - get(a)) to get the cost
class Solution:
    def createSortedArray(self, A):
        m = max(A)
        c = [0] * (m + 1)

        def update(x):
            while x <= m:
                c[x] += 1
                x += x & (-x)
        def get(x):
            res = 0
            while x :
                res += c[x]
                x -= x & (-x)
            return res

        res = 0
        for i, a in enumerate(A):
            res += min(get(a - 1), i - get(a))
            update(a)
        return res % (10**9 + 7)
