func canJump(nums []int) bool {
    
    max_jump := 0
    for i,v := range nums{
        if i > max_jump {
            return false
        }
        if i + v > max_jump{
            max_jump = i + v
        }
        
        if max_jump >= len(nums) - 1{
            return true
        }
    }
    return true
    
}
