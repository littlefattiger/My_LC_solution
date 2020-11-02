#https://leetcode.com/problems/array-nesting/

# all the arr would only circulate once, it does not matter which one we begin, we can circulate all arrays. and we need to get the longest one.

# general idea, my original idea is too complex, but it can pass oj

def arrayNesting(self, nums: List[int]) -> int:
        d1 = dict()
        d3 = dict()
        for i,v in enumerate(nums):
            d1[i] = v
        
        self.res = 1
        def helper(index, d1, d2,d3, depth):
            
            if index in d3:
                return d3[index] + depth
            
            if index in d2:
                #print(index, depth)
                d3[index] = depth
                return depth
             
            
            d2[index] = d1[index]
            
            d3[index] =     helper(d2[index], d1, d2,d3, 1 + depth)
            return d3[index]
        
        n = len(nums)
        for i in range(n):
            #print(helper(i, d1, dict(),0))
            self.res = max(self.res, helper(i, d1, dict(),d3,0))
        return self.res
# effective one
# only circulate once, and use a seen array to track
    def arrayNesting(self, nums: List[int]) -> int:
        
        res = 0
        n = len(nums)
        seen = [False]*n
        for v in nums:
            cnt = 0
            while not seen[v]:
                cnt += 1
                seen[v] = True
                v = nums[v]
            res = max(res,cnt)
        return res
# space saving, using O(1)
    def arrayNesting(self, nums: List[int]) -> int:
        
        res = 1
        n = len(nums)
         
        for v in nums:
            cnt = 0
            while nums[v] != v:
                cnt += 1
                nums[v], v = v, nums[v]
                 
            res = max(res,cnt)
        return res
