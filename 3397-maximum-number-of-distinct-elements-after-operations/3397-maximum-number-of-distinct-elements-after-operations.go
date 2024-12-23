func maxDistinctElements(nums []int, k int) int {
    sort.Ints(nums)
    var curr int = nums[0] - k
    var n int = len(nums)
    var result int = 1
    for i := 1; i < n; i ++ {
        if (curr < nums[i] + k) {
            result ++
            curr = max(nums[i] - k, curr + 1)
        }
    }
    return result
}