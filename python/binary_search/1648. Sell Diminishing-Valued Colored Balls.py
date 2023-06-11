# You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

# The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

# You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

# Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        l = 0
        r =  max(inventory) 
        while l < r:
            m = (l + r) //2
            total_order = sum([x - m for x in inventory if x >=m])
            if total_order <= orders:
                r = m 
            else:
                l = m + 1
        ans = 0
        total_order = sum([x - l for x in inventory if x >l])
        orders -= total_order
        ans +=  l * orders
        ans += sum([(v + l + 1) *( v - l)//2 for v in inventory if v >l])
        return ans%(10 ** 9 + 7)
 
