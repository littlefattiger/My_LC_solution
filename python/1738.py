class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        m = len(matrix)
        n = len(matrix[0])
        r = 0
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
         
        for i in range(1,m + 1):
            for j in range(1, n + 1):
                dp[i][j] = matrix[i -1][j - 1] ^ dp[i - 1][j - 1] ^ dp[i - 1][j ] ^dp[i ][j - 1] 
                heappush(heap, dp[i][j])
        
        mm = heapq.nlargest(k, heap)
        #print(mm)
        return mm[-1]
        
  # it is a simple DP
