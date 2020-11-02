# https://leetcode.com/problems/maximum-width-ramp/
#the idea is not easy. Use a stack to keep an increasing stack from reverse order, if it is smaller, then using binary seach to seach the first one >= current value
# and also include the index in the array, and we can easily get the diff.
# the idea that findest the leffest position that current value is larger or equal to, the idea is great., and also reverse order, hard to think out. This solution refer some discussion

    def maxWidthRamp(self, A: List[int]) -> int:
        res = 0
        stack = []
        n = len(A)
        for i in range(n)[::-1]:
            if not stack or A[i] > stack[-1][0]:
                stack.append((A[i],i))
            else:
                j = stack[bisect_left(stack,(A[i], i))][1]
                res = max(res, j - i)
        return res
