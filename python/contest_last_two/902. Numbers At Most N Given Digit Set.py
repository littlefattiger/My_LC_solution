class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:

        digit_set = {int(v) for v in digits}

        def _count(n):
            @cache
            def dp(index, tight, lastDigit, leadingZero):
                if index == len(n):
                    if leadingZero:
                        return 0 in digit_set
                    return 1
                maxDigit = int(n[index]) if tight else 9
                ans = 0
                for d in range(1 + maxDigit):
                    nextTight = tight and d == maxDigit
                    nextLeadingZero = leadingZero and d == 0
                    if nextLeadingZero:
                        ans = (ans + dp(index + 1, nextTight, lastDigit, nextLeadingZero)) % (10 ** 9 + 7)
                    elif d in digit_set:
                        ans = (ans + dp(index + 1, nextTight, lastDigit, nextLeadingZero)) % (10 ** 9 + 7)
                return ans

            return dp(0, True, 0, True)

        return _count(str(n))  