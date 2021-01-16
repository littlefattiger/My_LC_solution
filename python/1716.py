class Solution:
    def totalMoney(self, n: int) -> int:
        base = 1
        amount = 1
        weekday = 1
        total = 0
        while n > 0:
            
            total += amount
            amount += 1
            n -= 1
            weekday += 1
            if (weekday - 1)%7 == 0:
                base += 1 
                amount = base
            
        return total
