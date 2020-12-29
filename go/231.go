func isPowerOfTwo(x int) bool {
    
    if x < 1{
        return false
    }
    
    for x!= 1 {
        next := x/2
        if next * 2 != x{
            return false
        }else{
            x = next
        }
    }
    
    return true
}
