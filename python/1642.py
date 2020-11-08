# https://leetcode.com/problems/furthest-building-you-can-reach/
# using heap to store number of ladder, if length is larger than ladder, then pop up for brick, if brick is less than 0, then return current position. IF all good, return n - 1
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
         
        heap = []
        n = len(heights)
        for i in range(n - 1):
            if heights[i + 1] <= heights[i]:
                continue
            
            diff = heights[i + 1] - heights[i]
            heappush(heap, diff)
            if len(heap) > ladders:
                v = heappop(heap)
                bricks -= v
            if bricks < 0:
                return i  
        return n - 1
