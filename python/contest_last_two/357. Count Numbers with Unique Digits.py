class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        m = 10 ** 9 + 7
        def _count(n):
            @cache
            def dp(index, lastDigit, leadingZero):
                if index == len(n):
                    return 1
                maxDigit = 9
                ans = 0
                for d in range(1 + maxDigit):
                    nextLeadingZero = leadingZero and d == 0
                    if nextLeadingZero:
                        ans = (ans + dp(index + 1, lastDigit, nextLeadingZero)) % (10 ** 9 + 7)
                    elif  not(lastDigit & (1<<d)):
                        ans = (ans + dp(index + 1, lastDigit | (1<<d)  , nextLeadingZero)) % (10 ** 9 + 7)
                return ans
            if n == "0":
                return 1
            return dp(0, 0, True)

        return _count(str(10 **n - 1))