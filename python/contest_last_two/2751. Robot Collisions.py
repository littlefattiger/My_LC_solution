class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        ids = []
        for i, pos in enumerate(positions):
            ids.append((pos, i))
        ids.sort()
        queue = []
        # print(ids)
        for pos, index in ids:

            if directions[index] == "R":
                queue.append(index)
            else:
                while queue:
                    r_val = healths[queue[-1]]
                    l_val = healths[index]
                    if r_val < l_val:
                        healths[index] -= 1
                        healths[queue.pop()] = 0
                    elif r_val == l_val:
                        healths[queue.pop()] = 0
                        healths[index] = 0
                        break
                    else:
                        healths[queue[-1]] -= 1
                        healths[index] = 0
                        break
            # print(queue)
        n = len(positions)
        ans = []
        for i in range(n):
            if healths[i] > 0:
                ans.append(healths[i])
        return ans





