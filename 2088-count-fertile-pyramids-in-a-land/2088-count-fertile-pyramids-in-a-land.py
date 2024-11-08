class Solution:
    def countPyramids(self, x: List[List[int]]) -> int:
        def helper(grid):
            m = len(grid)
            n = len(grid[0])
            # Max height of pyramidal plot
            mh = (n + 1) // 2
            # DP [height - 1][bottom][start_bottom]
            # Loop over each height
            dp = {}
            level_one_pyramid = dict()
            for i in range(m):
                level_one_pyramid[i] = grid[i]
            dp[1] = level_one_pyramid
            result = 0
            for h in range(2, mh + 1):
                l = 2 * h - 1
                current_level_pyramid = dict()
                for b_idx in range(h -1, m):
                    current_bottom = [0] * n
                    row = grid[b_idx]
                    # Find any consecutive 1-array with length 2 * h - 1
                    start = 0
                    for i in range(n):
                        if row[i]:
                            
                            if i + 1 - start >= l:
                                left_index = i - l + 1
                                if dp[h - 1][b_idx - 1][left_index + 1]:
                                    current_bottom[left_index] = 1 
                                    result += 1
                        else:
                            start = i + 1
                    current_level_pyramid[b_idx] = current_bottom
                dp[h] = current_level_pyramid
            return result
        return helper(x) + helper(x[::-1])