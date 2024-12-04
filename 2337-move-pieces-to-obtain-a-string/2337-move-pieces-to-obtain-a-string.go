func canChange(start string, target string) bool {
    if strings.ReplaceAll(start, "_", "") != strings.ReplaceAll(target, "_", ""){
        return false
    }
    var i, l, r int
    var n int = len(start)
    for i < n { 
        if start[i] == 'R' {
            r ++
        }
        if target[i] == 'L' {
            l ++
        }
        if start[i] == 'L' {
            if l <= 0 {
                return false
            } else {
                l --
            }
        }
        if target[i] == 'R' { 
            if r <= 0 {
                return false
            } else {
                r --
            }
        }
        i += 1
    }
    return true
}