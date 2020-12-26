func isPalindrome(x int) bool {
    if x < 0{
        return false
    }
    t := x
    ans := 0
    for x > 0 {
        ans = ans * 10 + x %10
        x = x/10
    }
    return ans == t
}
