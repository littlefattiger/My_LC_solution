func lengthOfLongestSubstring(s string) int {
     
    seen := make(map[rune]int)
    start := 0
    res := 0
    for i,v := range s{
        if index, ok := seen[v];ok {
            start = max( start , index + 1) 
        }
        res = max( res , i - start + 1) 
        seen[v] = i
    }
    return res
    
}

func max (a, b int) int{
    if a >= b{
        return a
    }
    return b
}
