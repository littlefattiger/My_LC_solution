# python need to use traditional DFS and binary search and in addition, we need to use prune, with flag = 1 to deal with symetry.

# 1, use dp, would TLE
# 2, use dfs and binary search, assign worker to deal with ubset states, would also TLE
# 3, use traditional dfs, and binary search. It is easy to prune, use a flag, to assign to worker = 0 obly once, meaning try only once.
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        
        #dp[0][0] = 0
 
        jobs.sort(reverse = True)
        def dfs( worker, limit, m):
            if  m >= n :
                return True
            flag = 0
            for j in range(k):
                if worker[j] + jobs[m] > limit:
                    continue
                if worker[j] == 0:
                    if flag:
                        continue
                    else:
                        flag = 1
                worker[j] += jobs[m]
                if dfs( worker, limit, m + 1) :
                    return True
                worker[j] -= jobs[m]

             
            return False
        
        #print(time_subset)
        low = 1
        high = sum(jobs) + 1
        
        
        
        while low < high:
            m = (low + high) // 2
            worker = [0]* k  
            if  dfs(worker, m, 0):
                high = m
            else:
                low = m + 1
        
        return low
    
        
        
