class Solution:
    def countPyramids(self, x: List[List[int]]) -> int:
        m = len(x)
        n = len(x[0])
        # Max height of pyramidal plot
        mh = min((n + 1) // 2, m)
        def helper(grid):
            # DP [row_index][height][start_bottom]
            # Current level result
            current_level = defaultdict(dict)
            # Loop over size-1 pyramid
            for i in range(n):
                current_level[1][i] = grid[0][i]
            result = 0
            for i in range(1, m):
                current = defaultdict(dict)
                row = grid[i]
                # Find any consecutive 1-array with length
                start = 0
                for j in range(n):
                    if row[j]:
                        current[1][j] = 1
                        # current[1][j] = 1
                        l = j + 1 - start
                        if l % 2 == 0:
                            start_index = start + 1
                        else:
                            start_index = start
                        for left_index in range(start_index, j - 1, 2):
                            level = (j - left_index)//2 + 1
                            if current_level[level - 1].get(left_index + 1, 0):
                                current[level][left_index] = 1 
                                result += 1
                    else:
                        start = j + 1
                current_level = current
            return result
        result1 = helper(x)
        print("Result 1", result1)
        result2 = helper(x[::-1])
        print("Reusult 2", result2)
        return result1 + result2
        # 0 1 1 1 0
        # 1 1 1 1 1
        # 1 1 1 1 1 
        # 1 0 1 0 1