MOD = 1_000_000_007
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        m = len(words[0])
        # A table to with struct as [index][from_idx]. Which will store the total char with equal to target[index] from from_idx to n - 1
        count_table = defaultdict(lambda: [0] * m)
        for i in range(n):
            if target[i] in count_table:
                continue
            for j in range(m - 1, -1, -1):
                count = 0
                for word in words:
                    if word[j] == target[i]:
                        count += 1
                count_table[target[i]][j] = count
                
        # Pick/drop DP
        @lru_cache(None)
        def dfs(index, current):
            if index == n:
                return 1
            if current == m:
                return 0
            char = target[index]
            return dfs(index, current + 1) + dfs(index + 1, current + 1) * count_table[char][current]
        return dfs(0, 0) % MOD