func mySqrt(x int) int {
    
    l := 1
    r := x
    for l < r{
        m := (l + r)/2
        if m * m >= x {
            r = m
        }else{
            l = m + 1
        }
    }
    if l * l > x {
        return l - 1
    }
    return l 
    
}
