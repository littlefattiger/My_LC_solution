class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        p1 = [1] * n
        p2 = [1] * n
        ans = 1
        for i in range(1, n):
            if nums1[i] >= nums1[i -1]:
                p1[i] = max(p1[i], p1[i -1] + 1)
            if nums2[i] >= nums2[i -1]:
                p2[i] = max(p2[i],p2[i -1] + 1)
            if nums1[i] >= nums2[i -1]:
                p1[i] = max(p1[i], p2[i -1] + 1)
            if nums2[i] >= nums1[i -1]:
                p2[i] = max(p2[i], p1[i -1] + 1)
            ans = max(ans, p1[i], p2[i])
        return ans


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        p11 = p12 = p21 = p22 = 1
        p1 = p2 = 1
        ans = 1
        for i in range(1, n):
            p11 = 1 if nums1[i] < nums1[i - 1] else p1 + 1
            p21 = 1 if nums1[i] < nums2[i - 1] else p2 + 1

            p22 = 1 if nums2[i] < nums2[i - 1] else p2 + 1
            p12 = 1 if nums2[i] < nums1[i - 1] else p1 + 1

            p1 = max(p11, p21)
            p2 = max(p12, p22)
            ans = max(ans, p1, p2)

        return ans