# all the arr would only circulate once, it does not matter which one we begin, we can circulate all arrays. and we need to get the longest one.
# general idea

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
