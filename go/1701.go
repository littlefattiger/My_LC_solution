func averageWaitingTime(customers [][]int) float64 {
    total_time := 0
    start := 0
    finish := 0
    for _, customer := range customers{
        first, second := customer[0], customer[1]
        if first > start{
            start = first
        }
        if finish > start{
            start = finish
        }
        finish = start + second
        total_time += finish - first
    }
    
    return float64(total_time)/float64(len(customers))
    
}
