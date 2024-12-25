func largestAltitude(gain []int) int {
    var count, result int = 0, 0
    for _, num := range gain {
        count += num
        result = max(result, count)
    }
    return result
}