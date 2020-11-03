# https://leetcode.com/problems/3sum-with-multiplicity/
# just think about there is 3 number, either 3 are the same or 2 are the same or they are all different
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        c = Counter(A)
         
        res = 0
        for a in c:
            for b in c:
                i = a
                j = b
                k = target - i - j
                if k not in c:
                    continue
                if i == k and k == j:
                    res += c[i] *(c[i] - 1) *(c[i] - 2) /6
                elif i == j and j != k:
                    res += c[i] *(c[i] - 1) *(c[k]  ) /2
                elif i < j and j < k:
                    res += c[i] *(c[j]  ) *(c[k]  )  
                    
        M = 10 ** 9 + 7
        return int(res) %M
