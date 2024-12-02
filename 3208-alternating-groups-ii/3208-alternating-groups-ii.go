func numberOfAlternatingGroups(colors []int, k int) int {
    colors = append(colors, colors[:k - 1]...)
    var l, curr, result int
    var n int = len(colors)
    for curr < n - 1 {
        x := curr + 1
        if colors[x] ^ colors[curr] == 1 {
            if x - l > k - 1 {
                l ++
            } 
        } else {
            l = x
        }
        curr = x
        if curr - l == k - 1 {
            result ++
        }
    }
    return result
}