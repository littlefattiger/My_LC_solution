
# This is similar to 2808. Minimum Seconds to Equalize a Circular Array.


# 424. Longest Repeating Character Replacement,


# 2024. Maximize the Confusion of an Exam
# https://leetcode.com/problems/find-the-longest-equal-subarray/solutions/3934172/java-c-python-one-pass-sliding-window-o-n/


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        freq = Counter()
        for i, num in enumerate(nums):
            freq[num] += 1
            # length i - l + 1
            ans = max(ans, freq[num])
            if ans + k < i - l + 1:
                freq[nums[l]] -= 1
                l += 1

        return ans


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        indices = defaultdict(deque)
        ans = 0

        for i, x in enumerate(nums):
            indices[x].append(i)

            while indices[x][-1] - indices[x][0] + 1 > len(indices[x]) + k:
                indices[x].popleft()

            ans = max(ans, len(indices[x]))

        return ans