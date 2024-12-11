func maximumBeauty(nums []int, k int) int {
    sort.Ints(nums)
    var left int
    var result int = 1
    var n int = len(nums)
    for i := 1; i < n; i ++ {
        num := nums[i]
        for (left < n) && (nums[left] + 2* k < num) {
            left ++
        }
        result = max(result, i - left + 1)
    }
    return result
}
