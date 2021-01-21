class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s) 
        @lru_cache(None)
        def dp_fun(i,j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dp_fun(i + 1,j - 1)
            else:
                return  min(dp_fun(i ,j - 1), dp_fun(i + 1,j )) + 1
        return dp_fun(0,n -1)
