# the idea is great, and use arth calculation here
# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.append(0)
        inventory.sort(reverse = True)
        res = 0
        n = len(inventory)
        k = 1
        for i in range(n - 1):
            if inventory[i] > inventory[i + 1]:
                if k *(inventory[i] - inventory[i + 1]) < orders:
                    orders -= k *(inventory[i] - inventory[i + 1])
                    res += k * (inventory[i] - inventory[i + 1] ) *(inventory[i] + inventory[i + 1] + 1)//2
                else:
                    n1, n2 = divmod(orders,k)
                    res += k * n1 *(inventory[i] + inventory[i] - n1 + 1)   // 2
                    res += n2 * (inventory[i] - n1)
                    return int(res) %(10**9 + 7)
            k += 1
            """
            10 | 8 | 6 | 4 | 2
             8 | 8 | 6 | 4 | 2
             6 | 6 | 6 | 4 | 2
             4 | 4 | 4 | 4 | 2
             2 | 2 | 2 | 2 | 2 
             0 | 0 | 0 | 0 | 0 
             
             """
# binary search idea is also cool. IT is to search a value that the price >k is sold and some of price k is sold.

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        l = 0
        r = max(inventory) 
        while l < r:
            m = (l + r)//2
            n_sell = sum(i - m for i in inventory if i >= m)
            if n_sell > orders:
                l = m + 1
            else:
                r = m
        value = 0
        for v in inventory:
            if v > l:
                value += (v - l) *(v + l + 1)//2
                orders -= (v - l)
        value += orders*l
        return value%(10**9 + 7)
