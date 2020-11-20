# simply use a dict to store order
# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = dict()
        
        for i,v in enumerate(order):
            d[v] = 26 - i
        
        def compare(s1, s2,d):
            i = 0
            n = min(len(s1), len(s2))
            while i < n:
                if s1[i] == s2[i]:
                    i += 1
                elif d[s1[i]] > d[s2[i]]:
                    return True
                elif d[s1[i]] < d[s2[i]]:
                    return False
            
            if len(s1) > len(s2) :
                return False
            else:
                return True
        
        for i in range(len(words) - 1):
            if not compare(words[i], words[i+1],d):
                return False
        return True
