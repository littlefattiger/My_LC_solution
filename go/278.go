func firstBadVersion(n int) int {
    l := 0
    r := n + 1
    for l < r {
        m := (l + r)/2
        if isBadVersion(m){
            r = m
        }else {
            l = m + 1
        }
    }
    return l
    
}
