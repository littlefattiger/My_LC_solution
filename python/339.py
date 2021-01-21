def depthSum( l):
    
    def helper(nl, level):
        res = 0
        n = len(nl)
        for i in range(n):
            if type(nl[i]) != list:
                res += nl[i] * level
            else:
                res += helper(nl[i], level + 1)
        return res
    return helper(l, 1)
l = [[1,1],2,[1,1]]
print(depthSum( l))
