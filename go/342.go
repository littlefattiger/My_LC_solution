func isPowerOfFour(n int) bool {
    if n < 1{
        return false
    }
    for n != 1 {
        prev := n/4
        if prev * 4 != n{
            return false
        }
        n = prev
    }
    return true
}
