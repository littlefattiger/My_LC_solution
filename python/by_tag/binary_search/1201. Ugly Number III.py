# An ugly number is a positive integer that is divisible by a, b, or c.

# Given four integers n, a, b, and c, return the nth ugly number.

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def computeGCD(x, y):
            while(y):
                x, y = y, x % y
            return abs(x)
        def compute_lcm(x, y):
            lcm = (x*y)//computeGCD(x,y)
            return lcm
        
        l = 0 
        r = 10 ** 10
        while l < r:
            m = (l + r)//2
            a_d = m//a
            b_d = m//b
            c_d = m//c
            ab_d = m//compute_lcm(a, b)
            bc_d = m//compute_lcm(c, b)
            ac_d = m//compute_lcm(a, c)
            abc_d = m//compute_lcm(a, compute_lcm(c, b))
            tot = a_d + b_d + c_d - ab_d - bc_d - ac_d + abc_d
            if tot >= n:
                r = m
            else:
                l = m + 1
        return l
