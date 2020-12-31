func rob(nums []int) int {
    
    n := len(nums)
    dp1 := make([]int, n )
    if n == 0{
        return 0
    }
    if n == 1 {
        return nums[0]
    }
    if n == 2{
        return max(nums[0], nums[1])
    }
    dp1[0] = nums[0]
    dp1[1] = max(nums[0], nums[1])
    for i:= 2; i < n - 1; i ++{
        dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
    }
    
    dp2 := make([]int, n )
    
    dp2[1] = nums[1]
    dp2[2] = max(nums[1], nums[2])
    for i:= 3; i < n  ; i ++{
        dp2[i ] = max(dp2[i-1], dp2[i-2] + nums[i ])
    }
    
    return max(dp1[n-2], dp2[n-1])
    
    
}


func max(a,b int) int {
    if a >= b{
        return a
    }
    return b
}
