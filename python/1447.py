#https://leetcode.com/problems/simplified-fractions/
# it is quite easy, you only need to append fraction which have gcd == 1

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        def gcd(a,b):
            if b > a:
                return gcd(b,a)
            if b == 0:
                return a
            return gcd(b,a%b)
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if gcd(i,j) == 1:
                    res.append(str(i) + '/' + str(j))
        return res
    # one line solution
    #def simplifiedFractions(self, n):
    #    return ['%d/%d' % (a, b) for a in range(1, n) for b in range(a + 1, n + 1) if math.gcd(a, b) == 1]
