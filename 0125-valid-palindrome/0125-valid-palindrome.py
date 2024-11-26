class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 48 - 57 
        # 97 - 122
        s = s.lower()
        s = [_s for _s in s if _s.isalnum()]
        return s == s[::-1]