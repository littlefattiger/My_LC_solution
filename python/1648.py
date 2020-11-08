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
