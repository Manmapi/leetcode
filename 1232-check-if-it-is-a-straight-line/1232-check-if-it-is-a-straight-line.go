func checkStraightLine(coordinates [][]int) bool {
    var i, j float64 = float64(coordinates[0][0]), float64(coordinates[0][1])
    var h, k bool = true, true
    for _, coor := range coordinates[1:] {
        x , y := float64(coor[0]), float64(coor[1])
        if x != i {
            h = false
        }
        if y != j { 
            k = false
        }
    }
    if h || k {
        return true
    }
    var slope =  (float64(coordinates[1][1]) - j) / (float64(coordinates[1][0]) - i)
    for _, coor := range coordinates[1:] {
        x , y := float64(coor[0]), float64(coor[1])
        if x == i && y != j { 
            return false
        }
        if x != i && y == j { 
            return false
        }
        if (y - j) / (x - i) != slope {
            return false
        }
    }
    return true
}