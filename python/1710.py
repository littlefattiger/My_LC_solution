class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        cur_unit = 0
        n = len(boxTypes)
        for i in range(n):
            b, u = boxTypes[i]
            if b <= truckSize:
                truckSize -= b
                cur_unit += b * u
            else:
                cur_unit += truckSize * u
                truckSize = 0 
        return cur_unit
