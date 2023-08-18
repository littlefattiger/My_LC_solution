from collections import Counter


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        right = Counter(nums)
        left = Counter()
        for i, num in enumerate(nums):
            left[num] += 1
            right[num] -= 1
            if left[num] * 2 > i + 1 and right[num] * 2 > (n - i - 1):
                return i

        return -1