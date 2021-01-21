class Solution:
    def findLeaves(self, root) -> bool:
    	res = []
        def helper(root,res):
        	if not root:
        		return -1
        	depth = 1 + max(helper(root.left, res),helper(root.right, res) )
        	while depth >= len(res):
        		res.append([])
        	res[depth].append(root.val)

        	return depth
        helper(root,res)

        return res
#Using dfs to know about its depth
