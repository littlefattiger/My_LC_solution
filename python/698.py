class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
         
        target = sum(nums) //k
        if sum(nums)%k != 0 or len(nums) < k:
            return False
        visit = [False] * len(nums)
        nums.sort(reverse = True)
        def helper(nums,pos,cursum,target, k):
            n = len(nums)
            if  cursum > target:
                return False
                # important pruning
            if k == 1:
                return True
            if cursum == target:
                return helper(nums,0,0,target, k - 1)
            for i in range(pos,n):
                if visit[i]:
                    continue
                visit[i] = True
                if helper(nums,i,cursum + nums[i] ,target, k):
                    return True
                
                visit[i] = False
            
            
            return False
        return helper(nums,0,0,target, k)
                
