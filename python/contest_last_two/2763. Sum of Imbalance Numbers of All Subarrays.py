# https://leetcode.cn/problems/sum-of-imbalance-numbers-of-all-subarrays/solutions/2327214/bao-li-mei-ju-pythonjavacgo-by-endlessch-2r7p/


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i, num in enumerate(nums):
            seen = set()
            seen.add(num)
            cnt = 0
            for j in range(i + 1, n):
                x = nums[j]
                if x in seen:
                    ans += cnt
                    continue
                cnt += 1
                if x - 1 in seen:
                    cnt -= 1
                if x + 1 in seen:
                    cnt -= 1
                seen.add(x)
                ans += cnt

        return ans

# 方法二：贡献法 ???