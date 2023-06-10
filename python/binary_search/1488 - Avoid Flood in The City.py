class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        fulllakes = dict()
        ans = [] 
        drydays = []
        for i, v in enumerate(rains):
            if v == 0:
                drydays.append(i)
                ans.append(1)
            else:
                if v in fulllakes:

                    it = bisect_left(drydays, fulllakes[v])
                    if it >= len(drydays):
                        return []
                    day = drydays[it]
                    ans[day] = v
                    del drydays[it]
                fulllakes[v] = i
                ans.append(-1)
        return ans
