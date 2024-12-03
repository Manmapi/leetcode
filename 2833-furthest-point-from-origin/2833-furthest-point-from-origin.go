func furthestDistanceFromOrigin(moves string) int {
    var l, r, flex int
    for _, value := range(moves){
        if value == 'L' { 
            l ++
        } else if value == 'R' {
            r ++
        } else {
            flex ++ 
        }
    }    
    return int(math.Abs(float64(l - r))) + flex
}