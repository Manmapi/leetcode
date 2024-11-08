class Solution:
    def countPyramids(self, x: List[List[int]]) -> int:
        m = len(x)
        n = len(x[0])
        # Max height of pyramidal plot
        mh = min((n + 1) // 2, m)
        def helper(grid):
            
            # DP [height - 1][bottom][start_bottom]
            # Loop over each height
            dp = {}
            # Current level result
            current_level = dict()
            # Loop over size-1 pyramid
            for i in range(m):
                current_level[i] = grid[i]
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
                                if current_level[b_idx - 1][left_index + 1]:
                                    current_bottom[left_index] = 1 
                                    result += 1
                        else:
                            start = i + 1
                    current_level_pyramid[b_idx] = current_bottom
                current_level = current_level_pyramid
            return result
        return helper(x) + helper(x[::-1])