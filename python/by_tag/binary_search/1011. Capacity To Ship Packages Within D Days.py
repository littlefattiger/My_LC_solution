# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) 
        r = sum(weights) + 1
        while l < r:
            m = (l + r)//2
            temp_ans = 1
            temp_weight = 0
            for weight in weights:
                if temp_weight + weight > m:
                    temp_ans += 1
                    temp_weight = weight
                else:
                    temp_weight += weight               
            if temp_ans >  days:
                l = m + 1
            else:
                r = m
        return l
