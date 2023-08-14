from functools import cache


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:

        def _count(n):
            @cache
            def dp(index, tight, lastDigit, leadingZero):
                if index == len(n):
                    return 1
                maxDigit = int(n[index]) if tight else 9
                ans = 0
                for d in range(1 + maxDigit):
                    nextTight = tight and d == maxDigit
                    nextLeadingZero = leadingZero and d == 0
                    if nextLeadingZero:
                        ans = (ans + dp(index + 1, nextTight, lastDigit, nextLeadingZero)) % (10 ** 9 + 7)
                    elif lastDigit == -1 or abs(lastDigit - d) == 1:
                        ans = (ans + dp(index + 1, nextTight, d, nextLeadingZero)) % (10 ** 9 + 7)
                return ans

            return dp(0, True, -1, True)

        return (_count(high) - _count(str(int(low) - 1))) % (10 ** 9 + 7)