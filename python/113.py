# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        
        def DFS (root,sum, out,res):
            if not root:
                return

            if not root.left and not root.right and root.val == sum:
                out.append(root.val)
                res.append(out[:])
                out.pop()
                return
                
                 
            out.append(root.val) 
            DFS(root.left, sum - root.val,  out,res )
            DFS(root.right, sum - root.val,  out, res )
            out.pop()
            
        DFS (root,sum, [],ans)
        
        return ans
            
