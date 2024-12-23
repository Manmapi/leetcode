MOD = 1_000_000_007
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        m = len(words[0])
        # A table to with struct as [index][from_idx]. Which will store the total char with equal to target[index] from from_idx to n - 1
        count_table = defaultdict(lambda: [0] * (m + 1))
        for i in range(n):
            if target[i] in count_table:
                continue
            for j in range(m - 1, -1, -1):
                count = 0
                for word in words:
                    if word[j] == target[i]:
                        count += 1
                count_table[target[i]][j] = count_table[target[i]][j + 1] + count
                
        # Pick/drop DP
        @lru_cache(None)
        def dfs(index, current):
            if index == n:
                return 1
            char = target[index]
            if index == n - 1:
                return count_table[char][current]
            if count_table[char][current] == 0:
                return 0
            result = 0
            for i in range(current, m):
                if count_table[char][i] == 0:
                    break
                if count_table[char][i] > count_table[char][i + 1]:
                    result += dfs(index + 1, i + 1) * (count_table[char][i] - count_table[char][i + 1])
            return result
        return dfs(0, 0) % MOD