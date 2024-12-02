func numberOfAlternatingGroups(colors []int) int {
    colors = append(colors, colors[:2]...)
    var l, curr, result int
    var n int = len(colors)
    for curr < n - 1 {
        x := curr + 1
        if colors[x] ^ colors[curr] == 1 {
            if x - l > 2 {
                l ++
            } 
        } else {
            l = x
        }
        curr = x
        if curr - l == 2 {
            result ++
        }
    }
    return result
}