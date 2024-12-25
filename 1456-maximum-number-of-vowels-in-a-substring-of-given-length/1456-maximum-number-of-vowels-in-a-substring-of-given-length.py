class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "o", "i", "u"}
        tracker = 0
        result = 0
        for i, c in enumerate(s):
            if c in vowels:
                tracker += 1
            if i >= k and s[i - k] in vowels:
                tracker -= 1
            result = max(tracker, result)
            if result == k:
                break
        return result