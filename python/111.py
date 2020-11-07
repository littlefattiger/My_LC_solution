# we can have dfs and BFS method to iterate the tree
# DFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
         
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if not root.right:
            return 1 + l
        elif not root.left:
            return 1 + r
        return 1 + min(l, r)

# BFS

class Solution:
    def minDepth(self, root: TreeNode) -> int:
         
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        level = 1
        while queue:
            size = len(queue)
            while size > 0:
                
                size -= 1
                node = queue.popleft()
                if not node.left and not node.right:
                    return level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
