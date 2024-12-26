class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        @cache
        def dp(i, j):
            if j >= m:
                return max(0, n - i)
            if i >= n:
                return max(0, m - j)
            if word1[i] == word2[j]:
                return min(
                    dp(i + 1, j + 1),
                    1 + dp(i + 1, j),
                    1 + dp(i, j + 1)
                )
            else:
                return min(
                    1 + dp(i + 1, j + 1),
                    1 + dp(i + 1, j),
                    1 + dp(i, j + 1)
                )
        return dp(0, 0)