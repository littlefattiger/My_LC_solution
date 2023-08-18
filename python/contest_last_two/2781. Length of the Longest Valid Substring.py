
#  Keyword 1 <= forbidden[i].length <= 10
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        seen = set(forbidden)
        ans = 0
        dp = [n]* (n + 1)
        for i in range(n-1, -1, -1):
            dp[i] = dp[i + 1]
            for j in range(i, min(i + 10, dp[i], n)):
                if word[i:j + 1] in seen:
                    dp[i] = j
                    break

            ans = max(ans, dp[i] - i)
        return ans