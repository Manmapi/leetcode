class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 48 - 57 
        # 97 - 122
        s = s.lower()
        accept_range = [*range(48, 58), *range(97, 123)]
        s = [_s for _s in s if ord(_s) in accept_range]
        return s == s[::-1]