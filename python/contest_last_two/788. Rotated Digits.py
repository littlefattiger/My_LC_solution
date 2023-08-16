class Solution:
    def rotatedDigits(self, n: int) -> int:

        def _count(n):
            @cache
            def dp(index, tight, lastDigit, leadingZero):
                if index == len(n):
                    if leadingZero:
                        return 0
                    for jj in [2, 5, 6, 9]:
                        if lastDigit & (1 << jj):
                            return 1
                    return 0
                maxDigit = int(n[index]) if tight else 9
                ans = 0
                for d in range(1 + maxDigit):
                    nextTight = tight and d == maxDigit
                    nextLeadingZero = leadingZero and d == 0
                    if nextLeadingZero:
                        ans = (ans + dp(index + 1, nextTight, lastDigit, nextLeadingZero)) % (10 ** 9 + 7)
                    elif d in {0, 1, 2, 5, 6, 8, 9}:
                        ans = (ans + dp(index + 1, nextTight, lastDigit | (1 << d), nextLeadingZero)) % (10 ** 9 + 7)
                return ans

            return dp(0, True, 0, True)

        return _count(str(n))  