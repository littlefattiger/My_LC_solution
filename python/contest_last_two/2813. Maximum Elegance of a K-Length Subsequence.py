class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key = lambda x: -x[0])
        ans = res = 0
        seen_category = set()
        profit_left = []
        for i, (profit, category) in enumerate(items):
            if i < k:
                res += profit
                if category in seen_category:
                    profit_left.append(profit)
            else:
                if category not in seen_category:
                    # 反悔贪心， popout the least one if exist
                    if profit_left:
                        res -= profit_left.pop()
                        res += profit
                    else:
                        break

            seen_category.add(category)
            ans = max(ans, res + len(seen_category) ** 2)
        return ans