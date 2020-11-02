# https://leetcode.com/problems/largest-values-from-labels/
# sort the array with label, and from largest to smallest, and use a hash table to keep track the number of same label

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        d = Counter()
        v2 = [ (v, l) for v, l in zip(values, labels)]
        v2.sort(key = lambda x: x[0],reverse = True)
        res = 0
        for i in range(len(values)):
            v,l = v2[i]
            if d[l] < use_limit:
                num_wanted -= 1
                d[l] += 1
                res += v
            else:
                continue
            
            if num_wanted == 0:
                return res
        return res
                
