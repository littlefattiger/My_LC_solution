# https://leetcode.com/problems/apply-operations-to-maximize-score/
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        @lru_cache(None)
        def getPrimeFactors(n):
            res = set()

            for i in range(2, isqrt(n) + 1):
                while n % i == 0:
                    res.add(i)
                    n //= i

            if n > 1: res.add(n)
            return len(res)

        scores = []
        for num in nums:
            scores.append(getPrimeFactors(num))

        M = 10 ** 9 + 7
        ans = 1

        temp = list(zip(list(range(len(nums))), nums))

        temp.sort(key=lambda x: (- x[1], x[0]))
        # print(temp)
        n = len(nums)

        nextGreater = [n] * n
        previousGreater = [-1] * n

        s = []
        for i in range(n - 1, -1, -1):
            while s and scores[s[-1]] <= scores[i]:
                s.pop()
            if s:
                nextGreater[i] = s[-1]
            s.append(i)

        s = []
        for i in range(n):
            while s and scores[s[-1]] < scores[i]:
                s.pop()
            if s:
                previousGreater[i] = s[-1]
            s.append(i)
        # print(scores)
        # print(previousGreater)
        # print(nextGreater)
        # print(temp)
        for id, num in temp:

            take = min(k, (id - previousGreater[id]) * (nextGreater[id] - id))
            k -= take
            # print(num, take)
            ans = ans * pow(num, take, M) % M
            if k == 0:
                break
        return ans