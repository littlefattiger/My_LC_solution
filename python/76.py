# https://leetcode.com/problems/minimum-window-substring/
# this is a very straightforward sliding window problem, expand right first, then shirink left

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        res = ""
        cnt = 0
        left = 0
        need = len(t)
        min_length = float('inf')
        for right in range(len(s)):
            if  s[right] in count:
                count[s[right]] -= 1
                if count[s[right]] >= 0:
                    cnt += 1
            while cnt == need:
                
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    res = s[left: right + 1]
                
                if s[left] in count:
                    count[s[left]] += 1
                    if count[s[left]] >  0:
                        cnt -= 1
                left += 1
        return res
