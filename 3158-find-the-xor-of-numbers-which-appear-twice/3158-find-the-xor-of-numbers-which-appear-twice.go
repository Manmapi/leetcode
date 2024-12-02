func duplicateNumbersXOR(nums []int) (result int) {
    track := make(map[int]int)
    for _, num := range nums { 
        track[num] ++ 
        if track[num] == 2 { 
            result ^= num
        }
    }
    return 
}