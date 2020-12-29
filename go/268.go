func missingNumber(nums []int) int {
    
    n := len(nums)
    x := n
    for j,v:= range nums{
        x ^= v
        x ^= j
        
    }
    
    return x
    
}
