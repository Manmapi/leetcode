class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited = set()
        n = len(s)
        def dfs(idx):
            if idx == n:
                return 0
            max_ = 0
            for i in range(idx, n):
                val = s[idx:i + 1]
                if val in visited:
                    continue
                visited.add(val)
                max_ = max(max_, 1 + dfs(i + 1))
                visited.remove(val)
            return max_
        return dfs(0)

        