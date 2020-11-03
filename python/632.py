#https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# this question is equavalent to problem 76, Minimum Window Substring, to find a sliding window that it include all charcters and here it includes all rows

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        need = [0] * n
        tot_list = []
        for i in range(n):
            for j in range(len(nums[i])):
                tot_list.append((nums[i][j], i) )
        tot_list.sort()
        start = 0
        min_length = float('inf')
        cnt = 0
        res = [-1, -1 ]
        
        for i in range(len(tot_list)):
            v,r = tot_list[i]
            if need[r] == 0:
                cnt += 1
            need[r] += 1
            while cnt == n and start <= i:
                v2, r2 = tot_list[start]
                if   v - v2 < min_length:
                    min_length = v - v2
                    res[0] = v2
                    res[1] = v
                
                need[r2] -= 1
                if need[r2] == 0:
                    cnt -= 1
                
                start += 1
        return res
                
                
        
        
