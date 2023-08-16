class Solution:
    def findIntegers(self, n: int) -> int:
        m = 10 ** 9 + 7

        def _count(n):
            @cache
            def dp(index, tight, lastDigit, leadingZero):
                if index == len(n):
                    return 1
                maxDigit = int(n[index]) if tight else 1
                ans = 0
                for d in range(1 + maxDigit):
                    nextTight = tight and d == maxDigit
                    nextLeadingZero = leadingZero and d == 0
                    if nextLeadingZero:
                        ans = (ans + dp(index + 1, nextTight, lastDigit, nextLeadingZero)) % (10 ** 9 + 7)
                    elif not d or (lastDigit != d):
                        ans = (ans + dp(index + 1, nextTight, d, nextLeadingZero)) % (10 ** 9 + 7)
                return ans

            return dp(0, True, 0, True)

        return _count(bin(n)[2:]) 