func minimumOperations(nums []int) (result int) {
    for _, num := range nums {
        if num % 3 != 0 {
            result ++
        }
    }
    return
}