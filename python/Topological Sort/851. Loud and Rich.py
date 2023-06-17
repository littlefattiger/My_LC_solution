# There is a group of n people labeled from 0 to n - 1 where each person has a different amount of money and a different level of quietness.

# You are given an array richer where richer[i] = [ai, bi] indicates that ai has more money than bi and an integer array quiet where quiet[i] is the quietness of the ith person. All the given data in richer are logically correct (i.e., the data will not lead you to a situation where x is richer than y and y is richer than x at the same time).

# Return an integer array answer where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]) among all people who definitely have equal to or more money than the person x.

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        res = [-1] * n
        g = defaultdict(list)

        for a, b in richer:
            g[b].append(a)
        def dfs(i):
            if res[i] >= 0:
                return res[i]
            res[i] = i
            for child in g[i]:
                if quiet[res[i]] > quiet[dfs(child)]: # here, this line, inline dfs
                    res[i] = res[child]
            return res[i]
        for i in range(n):
            dfs(i)
        return res
