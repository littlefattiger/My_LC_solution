func majorityElement(nums []int) int {
    x := -1
    cnt := 0
    for _,v := range nums{
        if cnt == 0 {
            x = v
            cnt = 1
        }else if x == v{
            cnt += 1
        } else  {
            cnt -= 1
        }
        
    }
    return x
    
    
}
