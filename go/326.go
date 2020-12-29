func isPowerOfThree(n int) bool {
    if n < 1{
        return false
    }
    for n != 1 {
        prev := n/3
        if prev * 3 != n{
            return false
        }
        n = prev
    }
    return true
}
