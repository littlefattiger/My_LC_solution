#pretty easy to use monotonic queue or heap
# https://leetcode.com/problems/jump-game-vi/
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float('-inf')] *n
        dp[0] = nums[0]
        # moving max for last k index
        deq = [0]
        
        for i in range(1, n):
            
            
            dp[i] = max(dp[i], dp[deq[0]]+ nums[i])
            while deq and dp[i] > dp[deq[-1]]:
                deq.pop()
            deq.append(i)
            if deq[0] == i - k:
                deq.pop(0)
            
            
             
        #print(dp)
        return dp[-1]
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float('-inf')] *n
        dp[0] = nums[0]
        # moving max for last k index
        heap = []
        heappush(heap, (- dp[0], 0))
        for i in range(1, n):
            if i > k:
                if heap[0][1] == i - k - 1:
                    heappop(heap)
            
            dp[i] = max(dp[i], -heap[0][0]+ nums[i])
            heappush(heap, (- dp[i], i))
        #print(dp)
        return dp[-1]
        
