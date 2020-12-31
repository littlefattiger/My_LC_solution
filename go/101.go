/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
    
    if root == nil{
        return true
    }
    return isSameTree(root.Left, root.Right)
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
    
    
    if p == nil && q == nil{
        return true
        
    }
    if p == nil || q == nil{
        return false
    }
    
    return (*p).Val == (*q).Val && isSameTree((*p).Left, (*q).Right) && isSameTree((*p).Right, (*q).Left) 
}
