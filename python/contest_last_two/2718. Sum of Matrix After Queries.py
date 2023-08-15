class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        col = dict()
        row = dict()
        ans = 0
        for (t, i, v) in queries[::-1]:
            if t == 0:
                if i not in row:
                    ans += v * (n - len(col))
                    row[i] = v

            else:
                if i not in col:
                    ans += v * (n - len(row))
                    col[i] = v

        return ans
