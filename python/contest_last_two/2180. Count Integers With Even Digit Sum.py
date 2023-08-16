class Solution:
    def countEven(self, n: int) -> int:

        def _count(n):
            @cache
            def dp(index, tight, lastDigit, leadingZero):
                if index == len(n):
                    if leadingZero:
                        return 0
                    return lastDigit % 2 == 0

                maxDigit = int(n[index]) if tight else 9
                ans = 0
                for d in range(1 + maxDigit):
                    nextTight = tight and d == maxDigit
                    nextLeadingZero = leadingZero and d == 0
                    if nextLeadingZero:
                        ans = (ans + dp(index + 1, nextTight, lastDigit, nextLeadingZero)) % (10 ** 9 + 7)
                    else:
                        ans = (ans + dp(index + 1, nextTight, lastDigit + d, nextLeadingZero)) % (10 ** 9 + 7)
                return ans

            return dp(0, True, 0, True)

        return _count(str(n))  