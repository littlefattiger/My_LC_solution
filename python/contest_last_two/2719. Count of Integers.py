from functools import cache


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        m = 10 ** 9 + 7

        def _count(n):
            @cache
            def dp(index, tight, lastDigit, leadingZero):
                if index == len(n):
                    if lastDigit <= int(max_sum) and lastDigit >= int(min_sum):
                        return 1
                    return 0
                maxDigit = int(n[index]) if tight else 9
                ans = 0
                for d in range(1 + maxDigit):
                    nextTight = tight and d == maxDigit
                    nextLeadingZero = leadingZero and d == 0
                    if nextLeadingZero:
                        ans = (ans + dp(index + 1, nextTight, lastDigit, nextLeadingZero)) % (10 ** 9 + 7)
                    elif lastDigit + d <= int(max_sum):
                        ans = (ans + dp(index + 1, nextTight, lastDigit + d, nextLeadingZero)) % (10 ** 9 + 7)
                return ans

            return dp(0, True, 0, True)

        return (_count(num2) - _count(str(int(num1) - 1))) % (10 ** 9 + 7)
