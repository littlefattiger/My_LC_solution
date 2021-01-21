# use a list to store info, then know the level

def depthSum( l):
    res = [0]
    def helper(nl, level,res):
         
        n = len(nl)
        while len(res) <= level:
            res.append(0)
        for i in range(n):
            if type(nl[i]) != list:
                res[level] += nl[i]  
            else:
                helper(nl[i], level + 1,res)
        #print(nl)
        return res
    helper(l, 1,res)
    n = len(res) 
    ans = 0
    # [[0],[2],[4]]
    # n = 3
    # level = 2
    for i in range(1, n):
        ans += res[i] * (n - 1 - (i - 1)) 
    return ans
l = [1,[4,[6]]]
print(depthSum( l))
