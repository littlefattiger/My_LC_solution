# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in ascending order, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

# You must write an algorithm that runs in logarithmic time.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0     
        n = len(citations)
        r = n
        if n == 0:
            return 0
        while l < r:
            m = (l + r)//2
            if citations[m] >= n - m:
                r = m
            else:
                l = m + 1
        return n - l
