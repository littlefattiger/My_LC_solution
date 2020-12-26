func twoSum(nums []int, target int) []int {
    
    reserve := make(map[int] int)
    for i,v := range nums {
        if val, ok:= reserve[target - v]; ok{
            return []int{i, val}
        }
        reserve[v] = i
        
    }
    return []int{-1, -1}
    
}
