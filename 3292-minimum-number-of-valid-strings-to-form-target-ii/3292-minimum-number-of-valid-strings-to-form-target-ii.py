class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        def prefix_function(s: str):
            n = len(s)
            pi = [0] * n
            for i in range(1, n):
                j = pi[i - 1]
                while j > 0 and s[i] != s[j]:
                    j = pi[j - 1]
                if s[i] == s[j]:
                    j += 1
                pi[i] = j
            return pi
        n = len(target)
        jump = [0] * (n + 1)
        for word in words:
            pi = prefix_function(word + "#" + target)
            n_ = len(word)
            for i in range(n + 1):
                index = i + n_
                jump[i] = max(jump[i], pi[index])
        l = n
        result = 0
        while l and jump[l]:
            l -= jump[l]
            result += 1
        return result if l == 0 else -1