# 这题数学太多了， 想法很简单， 没什么意思

# https://leetcode.com/problems/orderly-queue/

class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K > 1:
            return ''.join(sorted(list(S)))
        # K == 1
        res = S
        for i in range(len(S)):
            S = S[1:] + S[0]
            res = min(res, S) 
        return res
