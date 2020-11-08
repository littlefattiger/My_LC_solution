# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# using a map to calculate the value less than current value but did not exist, we can also use a stack to do so

class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        l = list(count.values())
        res = 0
        seen = set()
        for v in l:
            while v in seen:
                v -= 1
                res += 1
            if v:
                seen.add(v)    
        return res
