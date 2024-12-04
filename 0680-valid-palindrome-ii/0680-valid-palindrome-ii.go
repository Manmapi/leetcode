func sol(s string, count int) bool {
    var l int = 0
    var r int = len(s) - 1
    for l <= r { 
        if s[l] != s[r] {
            if count > 0 {
                return sol(s[l + 1:r + 1],  count - 1) || sol(s[l:r], count - 1) 
            } else {
                return false
            }
        }
        l ++
        r --
    }    
    return true
}
func validPalindrome(s string) bool {
    return sol(s, 1)
}