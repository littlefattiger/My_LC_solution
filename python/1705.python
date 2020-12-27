# consider to use heap to store the apple die first

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        heap = []
        res = 0
        i = 0
        while True:
            
            if i < n:
                heappush(heap, (i + days[i] - 1, apples[i]))
            while heap and heap[0][0] < i:
                heappop(heap)
            if heap:
                out, apple = heappop(heap)
                res += 1
                apple -= 1
                if apple > 0:
                    heappush(heap, (out, apple))
            i += 1
            
            if i >= n and not heap:
                break
        return res
            
